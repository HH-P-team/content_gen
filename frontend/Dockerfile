FROM node:lts-alpine

RUN echo $REACT_APP_SERVER_API

WORKDIR /opt/app

COPY ./frontend/package.json ./
COPY ./.env .

ENV NODE_OPTIONS="--max-old-space-size=4096"

RUN npm install --legacy-peer-deps

COPY ./frontend .

RUN npm run build

EXPOSE ${FRONTEND_PORT}

CMD ["npm", "start"]