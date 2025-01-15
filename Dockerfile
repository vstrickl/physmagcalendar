### This file defines the application's image content ###

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user and group
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m appuser

# Setup working directory
WORKDIR /src

# Install dependencies
COPY app/requirements.txt /src/app/
RUN pip install --no-cache-dir -r /src/app/requirements.txt

# Copy project
COPY . /src/

# Make the check_code.sh script executable
RUN chmod +x /src/sdlc/check_code

# Change ownership of /src to the non-root user
RUN chown -R appuser:appgroup /src

# Switch to the non-root user
USER appuser

# Debug PATH after switching to appuser
RUN echo "PATH after switch: $PATH"
RUN ls /usr/local/bin
RUN which gunicorn

# Enable static file caching
RUN python app/manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Start the Django server
ENTRYPOINT ["/src/cmd/run"]