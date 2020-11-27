FROM node:15.3.0-alpine

WORKDIR /usr/srs/app

COPY ./frontend/package*.json ./
COPY ./frontend/webpack.config.js ./

RUN npm install

COPY ./frontend/src ./src
COPY ./frontend/public ./public

#RUN npm run-script build

EXPOSE 5000

ENV HOST=0.0.0.0

CMD ["npm","start"]

