FROM python:3.9.1-alpine

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PORT=8000 \
    WEB_CONCURRENCY=3

RUN pip install --upgrade pip 

COPY ./requirements.txt .

RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]
