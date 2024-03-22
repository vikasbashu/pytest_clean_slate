FROM ubuntu:latest
WORKDIR .
COPY . .
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv
ENTRYPOINT ["sh", "./req_install.sh"]
