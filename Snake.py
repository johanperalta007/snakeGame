import pygame
import time
import random

# Inicializa pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamaño de la ventana
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake Game')

# Configuración de la serpiente
tamaño_serpiente = 10
velocidad_serpiente = 15

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)

def mostrar_puntuacion(puntuacion):
    texto = fuente.render("Puntuación: " + str(puntuacion), True, negro)
    pantalla.blit(texto, [0, 0])

def dibujar_serpiente(tamaño_serpiente, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, negro, [x[0], x[1], tamaño_serpiente, tamaño_serpiente])

def juego():
    fin_juego = False
    fin_del_juego = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamaño_serpiente) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_serpiente) / 10.0) * 10.0

    while not fin_juego:

        while fin_del_juego:
            pantalla.fill(azul)
            mensaje = fuente.render("Perdiste! Presiona C para jugar de nuevo o Q para salir", True, rojo)
            pantalla.blit(mensaje, [ancho / 6, alto / 3])
            mostrar_puntuacion(longitud_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fin_juego = True
                        fin_del_juego = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_serpiente
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_serpiente
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_serpiente
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_serpiente
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            fin_del_juego = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_serpiente, tamaño_serpiente])
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)
        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                fin_del_juego = True

        dibujar_serpiente(tamaño_serpiente, lista_serpiente)
        mostrar_puntuacion(longitud_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_serpiente) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_serpiente) / 10.0) * 10.0
            longitud_serpiente += 1

        pygame.time.Clock().tick(velocidad_serpiente)

    pygame.quit()
    quit()

juego()