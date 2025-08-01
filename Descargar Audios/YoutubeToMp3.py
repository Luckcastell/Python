import yt_dlp
import os

def main():
    # Solicitar al usuario el enlace del video
    link = input("Inserta el link del video de YouTube para descargar en MP3: ")

    # Carpeta para guardar los MP3s
    output_folder = "C:\Users\lucac\Downloads\descargas mp3"
    os.makedirs(output_folder, exist_ok=True)  # Crear carpeta si no existe

    # Opciones para yt-dlp para extraer audio y convertirlo a mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{  # Convertir el audio a mp3 usando ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
        'noplaylist': True,  # No descargar playlists completas
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Descargando y convirtiendo a MP3...")
            ydl.download([link])
        print(f"\n¡Descarga completada! Los archivos MP3 están en la carpeta: {output_folder}")
    except Exception as e:
        print("Se produjo un error al descargar el video:", e)

if __name__ == "__main__":
    main()

