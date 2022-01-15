FROM node:16.13.2

SHELL ["/bin/bash", "-c"]

WORKDIR /usr/src/app

EXPOSE 3000

COPY package.json ./
RUN npm install

COPY . .
