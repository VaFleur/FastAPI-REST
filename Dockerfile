FROM python:3.11

LABEL authors="Anton Zhilinsky"

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

#Install requirements via pip
#COPY requirements.txt .

#RUN pip install -r requirements.txt
#End of pip usage

#Install requirements via pipenv
COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip

RUN pip install pipenv && pipenv install
#End of pipenv usage

COPY . .

RUN chmod a+x docker/*.sh

#CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000