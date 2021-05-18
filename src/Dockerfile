FROM python:3.9.1-alpine

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/usr/src/app \
    PORT=8000 \
    WEB_CONCURRENCY=3

RUN pip install --upgrade pip 

COPY ./requirements.txt .

RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# USER postgres

COPY . .

EXPOSE 5432

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
