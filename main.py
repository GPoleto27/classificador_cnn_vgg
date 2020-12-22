from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.applications.vgg16 import VGG16

from cv2 import cv2
from numpy import expand_dims
from classes import cars

import argparse

# Adiciona os argumentos
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--video_source', dest='video_source', help="Arquivo de origem do vídeo", default="video.mp4")
args = parser.parse_args()

# Altere essa variável para utilizar outros videos ou câmeras
video_source = args.video_source

# Define a fonte de captura de vídeo
cap = cv2.VideoCapture(video_source)

# Lê o primeiro quadro
success, img = cap.read()

# Cria uma caixa limitante com o input do mouse
bounding_box = cv2.selectROI("Classificador", img, False)

x, y, w, h = (bounding_box[i] for i in range(4))

end_x = x + w
end_y = y + h

# Define o modelo como VGG16 com os pesos da rede imagenet
model = VGG16(weights='imagenet')

result = cv2.VideoWriter('result.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (1280, 720))

while True:
    # Lê um frame
    success, img = cap.read()

    # Se ler o frame com sucesso
    if success:
        # Recorta a área de interesse
        cropped = img[y:end_y, x:end_x]

        # Converte a imagem para o padrão PIL
        img_array = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
        img_array = cv2.resize(img_array, (224, 224))

        # Expande uma dimensão do array que representa a imagem
        img_array = expand_dims(img_array, axis=0)
        # Pré-processa o array
        img_array = preprocess_input(img_array)

        # Realiza as predições
        features = model.predict(img_array)
        # Decodifica as predições
        predictions = decode_predictions(features)

        # Retira o label e a probabilidade da classe mais provável
        label = predictions[0][0][1]
        probability = predictions[0][0][2]

        # Se o label está presente na lista de carros definida no arquivo classes.py
        if label in cars:
            # Insere texto verde na imagem
            cv2.putText(img, "Carro", (25, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.putText(img, str(round(probability * 100)) + "%", (25, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Desenha um retângulo verde na área de interesse
            cv2.rectangle(img, (x, y), (end_x, end_y), (0, 255, 0), 2)
        
        # Caso não estiver na lista
        else:
            # Insere texto vermelho na imagem
            cv2.putText(img, f'Outro', (25, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # Desenha um retângulo vermelho na área de interesse
            cv2.rectangle(img, (x, y), (end_x, end_y), (0, 0, 255), 2)

        # Exibe a imagem processada
        cv2.imshow("Classificador", img)

        result.write(img)
        
    if cv2.waitKey(1) == 27:
        break

cap.release()
result.release()
cv2.destroyAllWindows()
