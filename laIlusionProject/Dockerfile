FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache \
    build-base \
    mariadb-dev \
    && rm -rf /var/cache/apk/* \
    && wget https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz \
    && tar -xvzf pkg-config-0.29.2.tar.gz \
    && cd pkg-config-0.29.2 \
    && ./configure --prefix=/usr \
    && make && make install \
    && cd .. && rm -rf pkg-config-0.29.2.tar.gz pkg-config-0.29.2


WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000
