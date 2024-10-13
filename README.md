# 專案簡介

此專案是一個全端應用程式，包含前端和後端兩部分，旨在提供一個完整的捐款管理系統。專案使用了多種技術和框架來實現其功能，並且包含詳細的設定和配置。

## 後段

後端使用 Python 和 FastAPI 框架來構建，並且使用 SQLModel 來進行資料庫操作，Migration 使用 alembic。

## 前端

React：用於構建使用者介面。
Tailwind CSS：用於樣式設計。
TypeScript：用於靜態類型檢查。

## 啟動專案

* 前台專案
  * 後端

    ```bash
    python main.py
    ```

  * 前端

    ```bash
    npm run dev-admin
    ```

* 後台專案

  * 後端

    ```bash
    python main.py
    ```

  * 前端
  
    ```bash
    npm run dev-client
    ```

* 使用 Docker compose

  ```bash
  sudo ENVIRONMENT=production docker-compose up --build -d
  ```
