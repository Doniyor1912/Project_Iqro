FROM python:3.9

RUN mkdir project

WORKDIR /project


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install django
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
