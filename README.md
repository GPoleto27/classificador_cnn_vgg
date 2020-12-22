# Classificador CNN VGG

Aplicação em python de um classificador utilizando VGG para classificação de uma área de interesse de um vídeo.
[Video DEMO](https://youtu.be/Xt9MWlmFYDU)

Construa a imagem a partir do dockerfile ([Como?](https://docs.docker.com/engine/reference/commandline/build/))

Ou:

# Instalação e execução

## Clonando o Repositório

    $ git clone https://github.com/GPoleto27/classificador_cnn_vgg

## Instalando as dependências, configurações e pesos da rede

    $ cd classificador_cnn_vgg
    $ sudo chmod +x setup.sh
    $ ./setup.sh

## Execute a aplicação

    $ ./main.py

# Customização da aplicação

## Alterando a fonte do vídeo

Adicione o argumento _-v_ ou *--video_source*

> Altere essa variável para utilizar outros videos ou câmeras.

Você pode usar seu próprio arquivo de vídeo ou webcam.

Para arquivo, apenas modifique o nome do arquivo, para usar sua webcam, altere para um inteiro que irá indicar o índice de sua webcam.

> (Normalmente, se há apenas uma câmera, basta utilizar o valor 0).
