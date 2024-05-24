FROM nginx:latest


ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


COPY ./nginx/nginx_poxi.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/