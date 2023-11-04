# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container at /usr/src/app
COPY Pipfile Pipfile.lock ./

# Install dependencies from Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port the app runs on
# EXPOSE $PORT
EXPOSE 8000 

# Run the application using pipenv to ensure the correct Python environment
# CMD ["pipenv", "run", "python", "app.py"]
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "app:app"]


# build Docker image (huesli is name of image)
# sudo docker build -t huesli .

# run docker container 
# sudo docker run -d -p host_port:container_port your-image-name
# -d runs the container in detached mode (in the background).
# -p maps a port on your host to a port on the container. 
# sudo docker run -d -p 8000:8000 huesli

# update image 
# docker push your-username/your-app-name:tag