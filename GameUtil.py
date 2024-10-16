import pygame
import time
import pymunk
from enum import Enum
import pymunk.pygame_util

class Game:
    def __init__(self, width, height, space = None, debug = False):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.objetcs = []
        self.running = True
        self._last_updated = time.time()
        self.time_variation = 0
        self.space = space
        self.space = pymunk.Space()
        self.debug = debug
        self.background_color = (0,0,0)

    def set_background_color(self, color):
        self.background_color = color

    def play(self, handle_event, update,render, fps=60):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    handle_event(self, event)
            self
            # update game state
            self.time_variation = time.time() - self._last_updated
            if self.space:
                self.space.step(self.time_variation)
            for o in self.objetcs:
                o.update()
            update(self,self.time_variation)
            self._last_updated = time.time()
            # render
            self.screen.fill(self.background_color)
            for o in self.objetcs:
                self.screen.blit(o.image, o.rect)
            if self.debug:
                draw_options = pymunk.pygame_util.DrawOptions(self.screen)
                self.space.debug_draw(draw_options)
            render(self)
            pygame.display.flip()
            #
            self.clock.tick(fps)

    def set_gravity(self, gravity):
        self.space.gravity = gravity
        
    def add_game_object(self, gameObject ):
         gameObject.body = pymunk.Body(gameObject.mass, pymunk.moment_for_box(gameObject.mass, gameObject.image.get_size()))
         gameObject.body.position = pymunk.Vec2d(gameObject.rect.x, gameObject.rect.y)
         gameObject.body.body_type = gameObject.type.value
         gameObject.shape = pymunk.Poly.create_box(gameObject.body, gameObject.image.get_size() )
         self.objetcs.append(gameObject)
         self.space.add(gameObject.body, gameObject.shape)

    def add_game_objects(self, gameObjects):
        for o in gameObjects:
            self.add_game_object(o)


class SpriteSheet:
    def __init__(self, path, start=(0, 0), frame_size=(32, 32), frame_number=1):
        self.path = path
        self.start = start
        self.frame_size = frame_size
        self.frame_number = frame_number




class GameObjectType(Enum):
    DYNAMIC = pymunk.Body.DYNAMIC
    STATIC = pymunk.Body.STATIC
    KINEMATIC = pymunk.Body.KINEMATIC

class GameObject(pygame.sprite.Sprite):    
    def __init__(self, size, type=GameObjectType.DYNAMIC):
        super().__init__()

        self._position = (0,0)
        self._size = size
        self._type = type
        self._space = None
        self._mass = 1
        self._animation_speed = 0.2 
        self._animations = {}


        self._current_animation = None
        self._current_frame = 0
        self._last_updated = time.time()
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self.rect = pygame.Rect(value, self.size) 
        if hasattr(self, 'body'):
            self.body.position = pymunk.Vec2d(value[0], value[1])

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value
        self.rect = pygame.Rect(self.position, value) 
        if hasattr(self, 'body'):
            self.body.position = pymunk.Vec2d(value[0], value[1])

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
        if hasattr(self, 'body'):
            self.body.body_type = value.value
    
    @property
    def space(self):
        return self._space
    
    @space.setter
    def space(self, value):
        self._space = value
        if hasattr(self, 'body'):
            self.body.space = value

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, value):
        self._mass = value
        if hasattr(self, 'body'):
            self.body.mass = value

    @property
    def animation_speed(self):
        return self._animation_speed
    
    @animation_speed.setter
    def animation_speed(self, value):
        self._animation_speed = value
        self._last_updated = time.time()


    @property
    def animations(self):
        return self._animations
    
    @animations.setter
    def animations(self, value):
        self._animations = value
        self._last_updated = time.time()

    

    def add_animation(self, name, spriteSheet):
        # Load the image from the sprite sheet path
        sheet_image = pygame.image.load(spriteSheet.path).convert_alpha()

        frame_dimensions = [(spriteSheet.start[0] + i * spriteSheet.frame_size[0], spriteSheet.start[1], spriteSheet.frame_size[0], spriteSheet.frame_size[1]) for i in range(spriteSheet.frame_number)]
        frames = []
        for (x, y, width, height) in frame_dimensions:
            sprite = pygame.Surface((width, height), pygame.SRCALPHA)
            sprite.blit(sheet_image, (0, 0), (x, y, width, height))  # Use the loaded image here
            frames.append(sprite)
        self.animations[name] = frames

    def set_current_animation(self, name):
        self.current_animation = name
        self.current_frame = 0
        self.image = self.animations[self.current_animation][self.current_frame]
        self._last_updated = time.time() 
        


    def update(self):
        # Update sprite animation
        if time.time() - self._last_updated > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.current_frame]
            self._last_updated = time.time()

        # Update sprite position based on physics
        if hasattr(self, 'body'):
            self.rect.x = self.body.position.x - self.rect.width / 2
            self.rect.y = self.body.position.y - self.rect.height / 2

    def apply_force(self, force):
        self.body.apply_force_at_local_point(force)

    def set_velocity(self, velocity):
        self.body.velocity = velocity

    def set_velocity_x(self, velocity):
        self.body.velocity = (velocity, self.body.velocity.y)

    def set_velocity_y(self, velocity):
        self.body.velocity = (self.body.velocity.x, velocity)

    def create_clones(self, positions):
        return [self.create_clone(p) for p in positions]
    
    def create_clone(self, position):
        clone = GameObject(self.size, self.type)
        clone.position = position
        clone.mass = self.mass
        clone.animation_speed = self.animation_speed
        clone.animations = self.animations
        clone.set_current_animation(self.current_animation)
        return clone
    
    def is_on_ground(self):
        return self.body.velocity.y == 0


    
