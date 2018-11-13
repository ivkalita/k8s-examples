FROM python:3.7.1-alpine3.8

RUN apk update && \
    apk add --virtual .build-deps gcc musl-dev make

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY main.py /usr/src/app/

EXPOSE 8000

CMD ["python", "/usr/src/app/main.py"]
