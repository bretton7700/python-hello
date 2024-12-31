FROM python:3.12-bookworm

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
