import pygame
from GameUtil import  GameObject, Game, GameObjectType, SpriteSheet

# Cores RGB (Red, Green, Blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Criar um jogo com 800x600 pixels
game = Game(800, 600)

# Aplica a gravidade no jogo
# primeiro valor é a gravidade no eixo X
# segundo valor é a gravidade no eixo Y
game.set_gravity((0, 40))

# Define a cor de fundo do jogo
game.set_background_color(WHITE)

# Define a força do salto
VELOCIDADE_DE_SALTO = 50
VELOCIDADE_ANDAR = 50

personagem1 = GameObject(size=(32,32), type=GameObjectType.DYNAMIC)
personagem1.position = (100,100)
personagem1.add_animation("idle", SpriteSheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Idle (32x32).png", (0,0), (32,32), 10))
personagem1.add_animation("run", SpriteSheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Run (32x32).png", (0,0), (32,32), 10))
personagem1.set_current_animation("idle")

# cria um bloco
bloco = GameObject(size=(40,48), type=GameObjectType.STATIC)
bloco.position = (100,100)
bloco.add_animation("idle", SpriteSheet("sprites/PixelAdventure/Terrain/Terrain (16x16).png", (0,0), (48,48), 1))
bloco.set_current_animation("idle")

# cria varios blocos
blocos = bloco.create_clones([(0, 500), (48, 500) ])

game.add_game_object(personagem1)
game.add_game_objects(blocos)


# tratamento de eventos
def handle_game_event(game, event):
    # tratar direcao do personagem
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            personagem1.set_velocity_x(-VELOCIDADE_ANDAR)
            personagem1.set_current_animation("run")
            pass
        if event.key == pygame.K_RIGHT:
            personagem1.set_velocity_x(VELOCIDADE_ANDAR)
            personagem1.set_current_animation("run")
            pass
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            pass
        if event.key == pygame.K_a:
            pass
        if event.key == pygame.K_d:
            pass
        if event.key == pygame.K_w:
            pass
        if event.key == pygame.K_s:
            pass
        if event.key == pygame.K_SPACE:
             if personagem1.is_on_ground():
                 personagem1.set_velocity_y(-VELOCIDADE_DE_SALTO)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            personagem1.set_velocity_x(0)
            personagem1.set_current_animation("idle")
            pass
        if event.key == pygame.K_RIGHT: 
            personagem1.set_velocity_x(0)
            personagem1.set_current_animation("idle")
            pass
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            pass
        if event.key == pygame.K_a:
            pass
        if event.key == pygame.K_d:
            pass
        if event.key == pygame.K_w:
            pass
        if event.key == pygame.K_s:
            pass

def update_game_state(game, time_variation):
    pass


def render_sprites(game):
    pass
    

game.play(handle_game_event, update_game_state, render_sprites)


