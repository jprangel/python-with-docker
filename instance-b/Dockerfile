FROM jpolarix/python-with-docker

ENV PATH_JSON_W=''
RUN apk add --no-cache openrc openssh bash supervisor

RUN mkdir -p /run/openrc/
RUN touch /run/openrc/softlevel; rc-update add sshd; rc-status; /etc/init.d/sshd stop

COPY config/sshd_config /etc/ssh/
RUN ssh-keygen -A
RUN mkdir /root/.ssh
ADD config/supervisord.conf /etc/

WORKDIR /app

RUN mkdir -p bucket-w
COPY pythonwithdocker.pvt ./
ADD src/ ./src
COPY config/authorized_keys /root/.ssh/
RUN chmod 400 /root/.ssh/*
RUN gpg2 --import /app/pythonwithdocker.pvt

ENV PATH "$PATH:/root/.local/bin/"

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
