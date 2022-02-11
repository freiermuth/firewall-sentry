FROM python:3

# WARNING! Change to a different, longer, random token prior to deploying!
ENV TOKEN=XYZ

EXPOSE 8080

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./firewall-sentry/run.py" ]