
# Dockerfile for MRI Reconstruction Microservice

# This container packages the FastAPI inference service
# and the compressed sensing MRI reconstruction engine.
# It is designed for deployment on any container platform
# (Docker Desktop, Azure Container Apps, AWS ECS, etc.)


# Base image: Python runtime

FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container :

# Requirements first (better caching)
COPY requirements.txt .

# Then copy the rest of the application
COPY api_service.py .
COPY compressed_sensing_mri.py .
COPY tests ./tests


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose port for FastAPI (default: 8000)
EXPOSE 8000

# Start the FastAPI service using Uvicorn

# host 0.0.0.0 allows external access when deployed
# port 8000 matches the EXPOSE directive
CMD ["uvicorn", "api_service:app", "--host", "0.0.0.0", "--port", "8000"]
