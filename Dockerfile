# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy the text files and the Python script into the container
COPY IF.txt AlwaysRememberUsThisWay.txt scripts.py /home/data/

# Create output directory
RUN mkdir -p /home/data/output

# Run the script when the container starts
CMD ["python", "/home/data/scripts.py"]
