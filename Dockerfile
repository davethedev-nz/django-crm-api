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
echo "Running database migrations..."\n\
python manage.py migrate --noinput || echo "Migrations failed, continuing..."\n\
echo "Migrations complete!"\n\
echo "Starting gunicorn on port 8000"\n\
exec gunicorn crm_project.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 4 --timeout 120 --access-logfile - --error-logfile -\n\
' > /app/start.sh && chmod +x /app/start.sh

# Run the startup script
CMD ["/bin/bash", "/app/start.sh"]
