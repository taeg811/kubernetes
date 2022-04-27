FROM alpine:3.14
RUN apk add --update curl py-pip python3
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
EXPOSE 8088
CMD ["python3", "podexporter.py"]
