# Use Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Create a startup script that runs migrations then starts gunicorn
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Function to wait for postgres\n\
wait_for_postgres() {\n\
    echo "Waiting for postgres..."\n\
    for i in {1..30}; do\n\
        if python manage.py migrate --check > /dev/null 2>&1; then\n\
            echo "Postgres is ready!"\n\
            return 0\n\
        fi\n\
        echo "Postgres is unavailable - sleeping"\n\
        sleep 2\n\
    done\n\
    echo "Could not connect to postgres after 60 seconds"\n\
    return 1\n\
}\n\
\n\
# Wait for postgres and run migrations\n\
if wait_for_postgres; then\n\
    echo "Running database migrations..."\n\
    python manage.py migrate --noinput\n\
    echo "Migrations complete!"\n\
else\n\
    echo "Skipping migrations - database not available"\n\
fi\n\
\n\
echo "Starting gunicorn on port ${PORT:-8000}"\n\
exec gunicorn crm_project.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --threads 4 --timeout 120 --access-logfile - --error-logfile -\n\
' > /app/start.sh && chmod +x /app/start.sh

# Run the startup script
CMD ["/bin/bash", "/app/start.sh"]
