FROM python:3
EXPOSE 8080

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./firewall-sentry/ .

CMD [ "python3", "./run.py" ]