FROM python:3.12

WORKDIR /app

ENV ENVIRONMENT=production

RUN apt-get update && apt-get install -y netcat-openbsd curl

RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

CMD ["sh", "-c", "./wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT -- uvicorn main:app --host 0.0.0.0 --port 8000 --log-config log.ini"]
