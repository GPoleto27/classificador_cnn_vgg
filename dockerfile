FROM python:3
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y python3-pip git
RUN git clone https://github.com/GPoleto27/classificador_cnn_vgg \
    && cd classificador_cnn_vgg \
    && chmod +x setup.sh \
    && ./setup.sh
