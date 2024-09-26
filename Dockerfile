# Use an official Python runtime as a parent image
FROM python:3.9

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    libgtk-3-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-pulseaudio \
    && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r scoreboard_app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 63115

# Define environment variable
ENV NAME TennisScoreboard
ENV FLET_FORCE_WEB_SERVER 1
ENV PORT 63115

# Run main.py when the container launches
CMD ["python", "scoreboard_app/main.py"]