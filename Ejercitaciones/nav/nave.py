import pygame

pygame.init()
pygame.mixer.init()
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
pygame.display.set_caption("Nave Musical")
bg = pygame.image.load("fondo.png").convert()

nave = pygame.image.load("ufo.png").convert_alpha()
nave = pygame.transform.scale(nave,(150,150))
x, y = 400, 300
vel = 5

musica = pygame.mixer.music.load("cancion.mp3")
reproduciendo = False
mute = False
inicio = False
sound = pygame.mixer.Sound("sonido.mp3")

running = True
while running:
    clock.tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if reproduciendo:
                    vol_act = pygame.mixer.music.get_volume() + 0.1
                    print(vol_act)
                    pygame.mixer.music.set_volume(vol_act)
            if event.key == pygame.K_DOWN:
                if reproduciendo:
                    vol_act = pygame.mixer.music.get_volume() - 0.1
                    print(vol_act)
                    pygame.mixer.music.set_volume(vol_act)
                    if vol_act < 0:
                        pygame.mixer.music.set_volume(0.0)
                        print(pygame.mixer.music.get_volume())
            if event.key == pygame.K_SPACE:
                if reproduciendo:
                    pygame.mixer.music.pause()
                    reproduciendo = False
                else:
                    if inicio:
                        pygame.mixer.music.unpause()
                        reproduciendo = True
            if event.key == pygame.K_1:
                pygame.mixer.music.play(-1)
                reproduciendo = True
            if event.key == pygame.K_0:
                sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if y > -40:
            y -= vel
    if keys[pygame.K_s]:
        if y < 490:
            y += vel
    if keys[pygame.K_a]:
        if x > -10:
            x -= vel
    if keys[pygame.K_d]:
        if x < 650:
            x += vel         

    
    # # Limitar la nave dentro de la pantalla
    # nave_x = max(0, min(nave_x, 640-50)) # limitar en eje X
    # nave_y = max(0, min(nave_y, 360-50)) # limitar en eje Y

    # Dibujo
    screen.blit(bg, (0,0))         # primero el fondo
    screen.blit(nave, (x,y))       # luego la nave
    pygame.display.flip()

pygame.quit()
