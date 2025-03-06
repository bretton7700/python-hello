FROM python:3.12-bookworm

WORKDIR /app

COPY server.py .
CMD ["python", "server.py"]
