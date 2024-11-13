FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip

# Para instalar las dependencias del proyecto LOCAL.
#RUN pip install -r requirements.txt

# Instala los requisitos
RUN pip install --no-cache-dir -r ./laIlusionProject/requirements.txt

EXPOSE 8000
