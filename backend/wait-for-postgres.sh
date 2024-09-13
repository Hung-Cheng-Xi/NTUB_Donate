#!/bin/sh

while ! nc -z postgres_db 5432; do
  echo "等待 PostgreSQL 準備中..."
  sleep 1
done

echo "PostgreSQL 已準備好，啟動應用程式。"
