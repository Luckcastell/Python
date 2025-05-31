import cv2
from datetime import datetime

# Inicializa la cámara (0 es el índice de la cámara por defecto)
camara = cv2.VideoCapture(0)

# Verifica si la cámara se abrió correctamente
if not camara.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Captura un fotograma
ret, imagen = camara.read()

# Verifica si se capturó correctamente
if ret:
    # Muestra la imagen capturada
    cv2.imshow("Imagen Capturada", imagen)
    # Guarda la imagen en un archivo
    cv2.imwrite("foto_capturada.jpg", imagen)
    cv2.waitKey(0)  # Espera a que se presione una tecla
else:
    print("No se pudo capturar la imagen.")

# Libera la cámara
camara.release()
cv2.destroyAllWindows()
