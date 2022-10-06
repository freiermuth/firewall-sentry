FROM python:3
EXPOSE 8080

WORKDIR /usr/src/app

RUN apt update && \
    apt-get install -y nginx && \
    addgroup --gid 1000 fits && \
    useradd --uid 1000 --gid 1000 fits

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY --chown=fits ./src/firewall-sentry/ .
COPY --chown=fits ./src/nginx/nginx.conf /etc/nginx/
COPY --chown=fits ./src/bash/ .

# nginx
RUN touch /var/run/nginx.pid && \
    chown -R fits:fits /var/run/nginx.pid /var/log/nginx /var/lib/nginx/

EXPOSE 8080

USER fits

CMD [ "./entrypoint.sh" ]