FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y wget python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install requests

WORKDIR /app

COPY Section1/httprequests.py .

CMD ["python3", "/app/httprequests.py"]
