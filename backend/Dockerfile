FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD ["python", "run.py"]
COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh
CMD ["./wait-for-db.sh", "python", "run.py"]

