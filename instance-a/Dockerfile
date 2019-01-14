FROM jpolarix/python-with-docker

ENV PATH_JSON_R=''
ENV PATH_JSON_W=''

RUN apk add --no-cache openssh netcat-openbsd

WORKDIR /app

ADD bucket-r/ ./bucket-r
RUN mkdir /app/bucket-w
COPY requirements.txt ./
COPY pythonwithdocker.pub ./
ADD src/ ./src

RUN mkdir /root/.ssh
COPY id_rsa /root/.ssh/
COPY id_rsa.pub /root/.ssh/
RUN chmod 400 /root/.ssh/*
RUN pip install -r requirements.txt

ENV PATH "$PATH:/root/.local/bin/"

RUN gpg2 --import /app/pythonwithdocker.pub

ENTRYPOINT ["/usr/bin/python3", "/app/src/main.py"]
