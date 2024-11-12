FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip

# Para instalar las dependencias del proyecto LOCAL.
#RUN pip install -r requirements.txt

# Para instalar las dependencias del proyecto INSTANCIA.
RUN pip install -r ./laIlusionProject/requirements.txt

EXPOSE 8000