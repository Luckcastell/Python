import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import cv2
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def foto():
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
        # cv2.imshow("Imagen Capturada", imagen)
        # cv2.waitKey(0)  # Espera a que se presione una tecla
        # Guarda la imagen en un archivo
        cv2.imwrite("foto_capturada.jpg", imagen)
    else:
        print("No se pudo capturar la imagen.")
    # Libera la cámara
    camara.release()
    cv2.destroyAllWindows()

def send_email():
    # Configura los detalles del correo
    sender_email = "" # Ingresa tu correo electrónico
    receiver_email = "" # Ingresa el correo electrónico al que deseas enviar el correo
    password = "" # Asegúrate de que esta sea la contraseña de aplicación correcta
    log_line = ""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Crea el mensaje
    msg = MIMEMultipart()
    msg['Subject'] = "ALERTA DE SEGURIDAD " + now
    msg['From'] = sender_email
    msg['To'] = receiver_email
    # Cuerpo del mensaje
    body = now + " | Han iniciado sesión en el sistema |"
    msg.attach(MIMEText(body, 'plain'))
    # Adjuntar la imagen
    # foto_path = r"C:\Users\lucac\Escritorio\Nueva carpeta\Python\Proyectos de prueba\foto_capturada.jpg"
    # with open(foto_path, "rb") as attachment:
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f'attachment; filename= {"foto_capturada.jpg"}')
    #     msg.attach(part)
    # Envía el correo
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Correo enviado exitosamente.")
            log_line = f"{now} - Correo enviado a {receiver_email} - Éxito\n"
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        log_line = f"{now} - Correo a {receiver_email} - Error: {e}\n"
    # Guardar registro en archivo texto
    with open(r"C:\Users\lucac\Escritorio\Nueva carpeta\Python\Proyectos de prueba\registro_envios.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)

if __name__ == "__main__":
    foto()
    send_email()
