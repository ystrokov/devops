# Use the official Python image from Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /devops
WORKDIR /devops

# Install Flask
RUN pip install Flask psycopg2-binary Flask-SQLAlchemy

# Copy the project files into the container
COPY . /devops/

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
