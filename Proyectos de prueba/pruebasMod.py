import pygame
import os

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
screen_width, screen_height = 1195, 796  # Ajusta el tamaño según necesites
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ventana de Imagen")

# Cargar la imagen (asegúrate de que esté en el mismo directorio o proporciona la ruta correcta)
image_path = 'image.png'  # Cambia esto por el nombre de tu imagen
image = pygame.image.load(image_path)

# Cargar y reproducir el archivo de audio MP3
audio_path = 'inicio.mp3'  # Cambia esto por el nombre de tu archivo MP3
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

# Centrar la imagen en la ventana
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Llenar la pantalla con negro
    screen.fill((0, 0, 0))
    
    # Dibujar la imagen en la ventana
    screen.blit(image, image_rect)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Verificando si la música ha terminado
    if not pygame.mixer.music.get_busy():
        running = False

# Cerrar Pygame
pygame.quit()