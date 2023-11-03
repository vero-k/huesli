# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /src

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

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the application using pipenv to ensure the correct Python environment
# CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "myapp:app"]