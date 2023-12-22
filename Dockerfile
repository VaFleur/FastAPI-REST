FROM python:3.11

LABEL authors="Anton Zhilinsky"

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip

RUN pip install pipenv && pipenv install  --dev --system --deploy

COPY . .

RUN chmod a+x docker/*.sh
