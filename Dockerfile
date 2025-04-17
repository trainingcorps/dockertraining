# Use an official Python base image
FROM ubuntu:22.04 

RUN apt update -y && apt upgrade -y && apt install vim -y
# Set working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

RUN apt install python3-pip -y
# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the port that Uvicorn will run on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]