FROM python:3.6.12-alpine3.12

COPY . .

RUN pip install -r requirements.txt && \
    crontab crontab

ENTRYPOINT ["/usr/sbin/crond", "-f"]
