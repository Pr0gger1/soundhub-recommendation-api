FROM python:3.12-slim
WORKDIR /app

COPY . .
COPY .env ./.env

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 8888
ENTRYPOINT ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8888"]