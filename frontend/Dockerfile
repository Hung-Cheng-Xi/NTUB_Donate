# 使用 Node 構建 admin 和 client 的應用
FROM node:20.15.1 AS build-admin

WORKDIR /app

# 複製 package.json 和 package-lock.json 並安裝依賴
COPY package*.json ./
RUN npm install

# 複製專案文件並構建 admin 應用
COPY . .
RUN npm run build-admin  # 執行 admin 的 build 指令

# 使用 Node 構建 client 的應用
FROM node:20.15.1 AS build-client

WORKDIR /app

# 複製 package.json 和 package-lock.json 並安裝依賴
COPY package*.json ./
RUN npm install

# 複製專案文件並構建 client 應用
COPY . .
RUN npm run build-client  # 執行 client 的 build 指令

# 使用 Nginx 部署構建好的 admin 和 client 應用
FROM nginx:alpine

# 複製 Nginx 配置文件
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 複製 admin 和 client 構建的結果到 Nginx 的靜態文件目錄
COPY --from=build-admin /app/app/admin/dist /usr/share/nginx/html/admin
COPY --from=build-client /app/app/client/dist /usr/share/nginx/html/client
