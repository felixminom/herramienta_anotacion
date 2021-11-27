FROM ubuntu
RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y netcat-openbsd

ENV INSTALL_PATH /backend-docker
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod +x $INSTALL_PATH/docker-entrypoint.sh

CMD ["/bin/bash", "/backend-docker/docker-entrypoint.sh"]
