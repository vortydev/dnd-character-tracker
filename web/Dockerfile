FROM python:3.13-slim

RUN apt update -y && apt upgrade -y

# Set workdir
WORKDIR /app

COPY web/ /app/
COPY bin/ /app/bin/
COPY data/ /app/data/

# Ensure bin is importable
ENV PYTHONPATH=/app:/app/bin

# Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]
