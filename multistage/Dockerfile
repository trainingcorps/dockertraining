# ----- Stage 1: Builder -----
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --user -r requirements.txt

# ----- Stage 2: Runner -----
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/root/.local/bin:$PATH

# Set working directory
WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy app code
COPY . .

# Expose port (adjust as needed)
EXPOSE 8000

# Default command (adjust as needed)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
