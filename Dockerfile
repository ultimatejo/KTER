FROM python:3.11-alpine

# Set up environment variables for Python
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire application code
COPY . ./

# Expose the port your application will run on
EXPOSE 8080

# Specify the command to run on container start
#CMD ["python", "flask_app.py"]
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["flask_app.py" ]
