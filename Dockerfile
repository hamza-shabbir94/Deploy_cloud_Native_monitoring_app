# Use the offical Python image as the base image
FROM python:3.11-slim-buster

# Set the working dirextory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python Packages
#RUN apk add --no-cache build-base linux-headers
RUN apt-get update -y
RUN apt-get install build-essential -y
RUN pip install --upgrade pip 
RUN pip cache purge 
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the env variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flash app will run
EXPOSE 5000

# start the Flask app when the container is running
CMD ["flask", "run"]

# now we will going to crate the image form the this docker file: docker build -t my-flask-app .
# docker images     # to check the images is created
# then run 