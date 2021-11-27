FROM python:3.7

WORKDIR /Edrill
COPY . /Edrill

RUN pip3.7 install -r requirements.txt

RUN pip3.7 install websocket

RUN pip3.7 install websocket-client

ENTRYPOINT ["python"]
CMD ["demo_app.py"]