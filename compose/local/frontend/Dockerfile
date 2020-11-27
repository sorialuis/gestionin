FROM node:15.3.0-alpine

WORKDIR /usr/srs/app

COPY package*.json

RUN npm install

COPY ./src ./src
COPY ./public ./public

RUN npm run-script build

EXPOSE 5000

ENV HOST=0.0.0.0

CMD ["npm","start"]

