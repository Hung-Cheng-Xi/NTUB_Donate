FROM python:3.12

WORKDIR /app

ENV ENVIRONMENT=production

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

COPY wait-for-postgres.sh /app/wait-for-postgres.sh
RUN chmod +x /app/wait-for-postgres.sh

CMD ["sh", "-c", "./wait-for-postgres.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --log-config log.ini"]
