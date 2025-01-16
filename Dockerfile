### This file defines the application's image content ###

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user and group
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m appuser

# Install Node.js, npm, and build tools
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setup working directory
WORKDIR /src

# Install dependencies
COPY app/requirements.txt /src/app/
RUN pip install --no-cache-dir -r /src/app/requirements.txt

# Copy project
COPY . /src/

# Return to the Django project root
WORKDIR /src

# Install npm dep & React Components
WORKDIR /src/ui
RUN npm install
RUN npm run build

# Return to the Django project root
WORKDIR /src

# Change ownership of /src to the non-root user
RUN chown -R appuser:appgroup /src

# Switch to the non-root user
USER appuser

# Collect Django static files (includes React build files)
RUN python app/manage.py collectstatic --noinput

# Double check React files exist in Django project
RUN ls -a /src/app/static/react/.vite
RUN ls -a /src/app/static/react/assets 

# Expose the application port
EXPOSE 8000

# Start the Django server
ENTRYPOINT ["/src/cmd/run"]