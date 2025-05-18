FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
