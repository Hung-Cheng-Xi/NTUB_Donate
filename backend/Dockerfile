FROM python:3.12

WORKDIR /app

# 接收環境變數 ENVIRONMENT
ARG ENVIRONMENT

# 設置環境變數
ENV ENVIRONMENT=${ENVIRONMENT}

# 安裝 nc 工具（netcat-openbsd 版本）
RUN apt-get update && apt-get install -y netcat-openbsd

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用代碼
COPY . .

# 暴露應用程式的埠
EXPOSE 8000

# 複製並設置等待 PostgreSQL 的腳本
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
RUN chmod +x /app/wait-for-postgres.sh

# 最終啟動命令：使用等待 PostgreSQL 的腳本，然後啟動應用程式
CMD ["sh", "-c", "./wait-for-postgres.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --env-file .env.${ENVIRONMENT}"]
