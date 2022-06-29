# syntax=docker/dockerfile:1
FROM python
WORKDIR /code
ENV FLASK_APP=run_blog.py
ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

# Build an image starting with the Python 3.7 image.
# Set the working directory to /code.
# Set environment variables used by the flask command.
# Install gcc and other dependencies
# Copy requirements.txt and install the Python dependencies.
# Add metadata to the image to describe that the container is listening on port 5000
# Copy the current directory . in the project to the workdir . in the image.
# Set the default command for the container to flask run.