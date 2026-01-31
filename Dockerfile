FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run migrations and collect static files (optional for local dev but good for container readiness)
# Note: In a real scenario, you might run migrations in the entrypoint or manually.
# For this simple setup, we'll assume the user runs migrations or the DB is mounted.
# But since we copy everything including db.sqlite3 (if it exists and not ignored), it might be fine.
# Better to run collectstatic here.
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
