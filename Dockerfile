FROM nginx:alpine
WORKDIR /usr/share/nginx/html
ENV NGINX_PORT=80
RUN apk add --no-cache bash
COPY index.html ./index.html
VOLUME /var/log/nginx
ENTRYPOINT /docker-entrypoint.sh
EXPOSE 80
LABEL maintainer=example@example.com
CMD nginx -g 'daemon off;'