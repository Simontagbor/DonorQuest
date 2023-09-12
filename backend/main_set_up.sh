#!/bin/bash

# Run environment setup script
echo "Setting up the development environment..."
./set_up_env.sh

# Run database setup script
echo "Setting up the databases..."
./set_up_db.sh

# Provide instructions for running migrations
echo "Development environment and databases are set up."
echo "To apply database migrations, run the following commands:"
echo "3. Run migrations: python manage.py makemigrations"
echo "4. Apply migrations: python manage.py migrate"
echo "Now you can start working with your Django project! you can run it with 'python manage.py runserver'."
