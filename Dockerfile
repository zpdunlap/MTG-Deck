FROM python:3

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./req.txt /app/req.txt

WORKDIR /app

RUN pip install -r req.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]