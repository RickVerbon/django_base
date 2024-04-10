FROM python:3.12

# Create a non-root user
RUN useradd -m bwayne

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Switch to non-root user for installation
USER bwayne


# Add the directory to PATH
ENV PATH="/home/bwayne/.local/bin:${PATH}"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]