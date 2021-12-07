# Step 1

FROM node:10-alpine as build-step

RUN mkdir /app

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

RUN npm run build

RUN npm install -S react-bootstrap

RUN npm install -S react-router-dom

RUN npm install -S recharts


# Stage 2

FROM nginx:1.17.1-alpine

COPY --from=build-step /app/build /usr/share/nginx/html