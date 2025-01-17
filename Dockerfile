### This file defines the application's image content ###

# Install npm dep & React Components
FROM node:20-slim AS node-builder
WORKDIR /src/ui
COPY ui/package*.json ./
RUN npm install
COPY ui/ .

# Vite will build to /src/app/static/react based on your config
RUN npm run build

FROM python:3.12-slim AS final
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV WEB_CONCURRENCY=1

# Create a non-root user and group
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m appuser

# Install Node.js, npm, and build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup working directory
WORKDIR /src

# Install dependencies
COPY app/requirements.txt /src/app/
RUN pip install --no-cache-dir -r /src/app/requirements.txt

# Copy project files
COPY . /src/

# Copy the built React files from node-builder stage
COPY --from=node-builder /src/app/static/react /src/app/static/react

# Change ownership of /src to the non-root user
RUN chown -R appuser:appgroup /src

# Switch to the non-root user
USER appuser

# Collect Django static files (includes React build files)
RUN python app/manage.py collectstatic --noinput

# Double check React files exist in Django project
RUN ls -a /src/app/static/react/.vite
RUN ls -a /src/app/static/react/assets 

RUN chmod +x /src/sdlc/check_env
RUN /src/sdlc/check_env

# Expose the application port
EXPOSE 8000

# Start the Django server
ENTRYPOINT ["/src/cmd/run"]