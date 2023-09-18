# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE backend.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django project into the container
COPY . /app/

# Expose the port the application runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
