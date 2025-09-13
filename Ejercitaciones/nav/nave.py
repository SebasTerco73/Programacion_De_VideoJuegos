import pygame

pygame.init()

# Configuración
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Fondo (imagen o color)
bg = pygame.image.load("nav/fondo.png").convert()

# Nave
nave = pygame.image.load("nav/nave.png").convert_alpha()
x, y = 400, 300
vel = 5

running = True
while running:
    clock.tick(60)  # FPS: controla la velocidad del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    
    # # Limitar la nave dentro de la pantalla
    # nave_x = max(0, min(nave_x, 640-50)) # limitar en eje X
    # nave_y = max(0, min(nave_y, 360-50)) # limitar en eje Y

    # Dibujo
    screen.blit(bg, (0,0))         # primero el fondo
    screen.blit(nave, (x,y))       # luego la nave
    pygame.display.flip()

pygame.quit()