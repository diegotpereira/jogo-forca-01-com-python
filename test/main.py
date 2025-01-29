import pygame
import random

pygame.init() 

pygame.display.set_caption("Jogo da Cobra em Pythom")

largura, altura = 1280, 700

tela = pygame.display.set_mode((largura, altura))

preta = (0, 0, 0)

branca = (255, 255, 255)

vermelho = (255, 0, 0)

verde = (0, 255, 0)

tamanho_quadrado = 20

velocidade_jogo = 15

def desenhar_cobra(tamanho, pixels):

            for pixel in pixels:

                pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def gerar_comida():

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0

    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):

    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])


def rodar_jogo(): 
    
    fim_jogo = False

    x = largura / 2

    y = altura / 2

    velocidade_x = 0

    velocidade_y = 0

    tamanho_cobra = 1

    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
           
        #    pass

        tela.fill(preta)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                fim_jogo = True

        
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        pygame.display.update()

        
        # pixels.append([x, y])

        # if len(pixels) > tamanho_cobra:

        #     del pixels[0]


        # for pixel in pixels[:-1]:
             
        #      if pixel == [x, y]:
                  
        #           fim_jogo = True

             


        # desenhar_cobra(tamanho_quadrado, pixels)





rodar_jogo()

