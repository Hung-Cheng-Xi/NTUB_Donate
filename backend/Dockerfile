FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd curl

RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["sh", "-c", "./wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT -- alembic  upgrade head && python main.py"]
