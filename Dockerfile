# Use an official Python image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /automation-api

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Ensure the environment variables are loaded from the .env file before running the tests
RUN pip install python-dotenv

# Copy the .env file into the container
COPY .env .env

# Run tests and generate an HTML report when the container starts
CMD ["python", "-m", "pytest", "tests/", "--html=tests/test_report.html"]
