import pygame
from pygame import Surface, Rect

# Variáveis de altura de largura da janela da aplicação
W_WIDTH = 576
W_HEIGHT = 324

# Inicializar a biblioteca PyGame
pygame.init()
print('setup start')
# Criando a janela do pygame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superfície
background: Surface = pygame.image.load('asset/background.png').convert_alpha()
player1: Surface = pygame.image.load('./asset/player1.png').convert_alpha()

# Obter o retângulo da superfície
background_rect: Rect = background.get_rect(left=0, top=0)
player1_react: Rect = player1.get_rect(left=100, top=100)

# Desenhar na janela em ordem (window)
window.blit(source=background, dest=background_rect)
window.blit(source=player1, dest=player1_react)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no jogo fps
clock = pygame.time.Clock()

# Carregar música e deixar ela tocando
pygame.mixer_music.load('./asset/music.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)

print('setup end')

print('loop start')
# Fechar a janela e encerrando o programa
while True:
    clock.tick(140)  # esse loop está acontecendo 140 vezes por segundo - fps
    # print(f'{clock.get_fps() :.0f}')  # verificar o fps sem casas decimais
    # Atualizando a tela para movimentar o background e o player1
    window.blit(source=background, dest=background_rect)
    window.blit(source=player1, dest=player1_react)
    pygame.display.flip()
    # Fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()
# Movimentar a espaçonave Player1 com as teclas w,s,d,a
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_react.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_react.centery += 1
    if pressed_key[pygame.K_d]:
        player1_react.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_react.centerx -= 1
        pass
