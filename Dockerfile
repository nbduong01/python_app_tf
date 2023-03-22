FROM python:3-alpine3.15
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3000

COPY . .
CMD python ./app.py

