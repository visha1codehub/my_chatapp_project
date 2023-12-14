# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:alpine3.19

# The enviroment variable ensures that the python output is set straight to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /conapp

# Set the working directory to /music_service
WORKDIR /conapp

# Copy the current directory contents into the container at /music_service
ADD . /conapp/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# port where the Django app runs within the container
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]