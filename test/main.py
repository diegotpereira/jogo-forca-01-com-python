import pygame
# import Randon

pygame.init() 

pygame.display.set_caption("Jogo da Cobra em Pythom")

largura, altura = 1280, 720

tela = pygame.display.set_mode((largura, altura))

preta = (0, 0, 0)

def rodar_jogo(): 
    
    fim_jogo = False

    while not fim_jogo:

        tela.fill(preta)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                fim_jogo = True


rodar_jogo()