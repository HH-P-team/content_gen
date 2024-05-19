FROM node:21-bullseye

WORKDIR /opt/app/

COPY package.json /opt/app/package.json
COPY public/ /opt/app/public/
ENV NODE_OPTIONS="--max-old-space-size=4096"

RUN npm install -g npm@10.4.0
RUN npm install --legacy-peer-deps

COPY src/ /opt/app/src/
