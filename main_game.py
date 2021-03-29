''' This is where the magic happens, here we will initiate the game, run the routines
and call the classes that were defined elsewhere, like Player and Enemy.'''
import pygame
import math
pygame.init()

# Determinando o tamanho da tela
janela_tamanho = pygame.display.set_mode((800,600))
# Dando o nome a janela
pygame.display.set_caption("Attack on Coronga")
# Carrega a imagem de fundo
img_fundo = pygame.image.load('fundo.png')
# Carrega imagem do personagem
img_personagem = pygame.image.load('doctor.png')
# Carrega imagem projetil
img_seringa = pygame.image.load('seringa.png')

# FPS do jogo
relogio = pygame.time.Clock()

# Definindo os status basicos do personagem
class Personagem:
    def __init__(self):
        self.pos_x = 150
        self.pos_y = 480
        self.tamanho_x = 64
        self.tamanho_y = 64
        self.velocidade = 10




#class Seringa:
#    def __init__(self, x, y, facing):
#        self.x = x
#        self.y = y
#        self.facing = facing
#        self.vel = 8 * facing
#    
#    def draw(janela_tamanho):
#        pygame.blit(img_seringa, (self.x, self.y))

# Draws background and updates the screen
def gameWindow():
    janela_tamanho.blit(img_fundo,(0,0))
    janela_tamanho.blit(img_personagem, (player.pos_x, player.pos_y))
    # Atualiza a tela para mostrar a imagem atual
    pygame.display.update()

# Atribui a variavel player os dados da classe Personagem
player = Personagem()

seringas =[]

#Loop principal, aqui ele vai escutar os comandos e permanecer o jogo rodando enquanto nao tentar fechar.
running = True
while running:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Escuta as teclas apertadas
    teclas = pygame.key.get_pressed()

    # Esquerda
    if teclas[pygame.K_LEFT] and player.pos_x > player.velocidade:
        player.pos_x -= player.velocidade

    # Direita
    if teclas[pygame.K_RIGHT]  and player.pos_x < 720:
        player.pos_x += player.velocidade
    
    gameWindow()


    


pygame.quit()