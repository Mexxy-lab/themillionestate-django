# Use an official Python runtime as a parent image
FROM python:3.9

# set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]