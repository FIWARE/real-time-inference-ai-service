# apis/Dockerfile

FROM python:3.9-slim-bullseye

WORKDIR /ml_api

COPY ./requirements.txt /ml_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ml_api/requirements.txt

COPY ./app /ml_api/app

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000" , "--reload"]