# Use Python 3.13 as the base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /src

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project structure to preserve package hierarchy
COPY src/ /src/src/
COPY tests/ /src/tests/

# Make port 8000 available to the world outside the container (if applicable)
EXPOSE 8000

# Set PYTHONPATH to include the project root
ENV PYTHONPATH=/src

# Run tests by default
CMD ["pytest", "tests/", "-v"]