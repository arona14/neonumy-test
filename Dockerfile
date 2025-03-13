# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Copy the entire project first
COPY . /app/

# Change to the project directory
WORKDIR /app/neonumy_album

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Set PYTHONPATH
ENV PYTHONPATH=/app/neonumy_album

# Collect static files
RUN poetry run python manage.py collectstatic --noinput

# Run gunicorn
CMD ["poetry", "run", "gunicorn", "neonumy_album.wsgi:application", "--bind", "0.0.0.0:8000"] 