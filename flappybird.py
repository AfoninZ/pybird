'''
Simplistic Flappy Bird clone game
for CodeLab
'''

import pygame
import pygame.freetype
from random import randint


DIST = 1500
GAP = 200


class Bird(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('bird.png').convert()
        self.rect = self.image.get_rect()

        self.x = 300
        self.y = 200

        self.vel = 0

    def update(self):
        self.vel += 0.003
        self.y += self.vel

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def jump(self):
        self.vel = -0.75


class Pipe(pygame.sprite.Sprite):
    def __init__(self, group, height, lower):
        super().__init__(group)
        self.image = pygame.image.load('pipe.png').convert()
        self.image = pygame.transform.scale(self.image, (60, height))
        self.rect = self.image.get_rect()

        self.x = 900
        if lower:
            self.y = size[1] - height
        else:
            self.y = 0

        self.rect.x = self.x
        self.rect.y = self.y

        self.vel = 0

    def update(self):
        self.x -= 0.25

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)


pygame.init()
size = width, height = 800, 600

screen = pygame.display.set_mode(size)
sprites = pygame.sprite.Group()

font = pygame.freetype.Font(pygame.freetype.match_font('sans'), 24)

bird = Bird(sprites)
pipes = []

score = 0
c = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bird.jump()

        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    bird.update()
    if bird.y < 0 or bird.y > height:
        # Out of game bounds; add ML stuff here
        score = 0
        bird.vel = 0
        sprites = pygame.sprite.Group()
        sprites.add(bird)
        pipes = []
        bird.y = 200

    for pipe in pipes:
        pipe.update()
        if pygame.sprite.collide_rect(bird, pipe):
            # Collision with pipe; add ML stuff here
            score = 0
            bird.vel = 0
            sprites = pygame.sprite.Group()
            sprites.add(bird)
            pipes = []
            bird.y = 200
        if pipe.x == 300 - 60 and pipe.y != 0:
            score += 1
        if pipe.x < -60:
            sprites.remove(pipe)
            pipes.remove(pipe)

    if c % DIST == 0:
        h = randint(0, 400)
        pipes.append(Pipe(sprites, h, False))
        pipes.append(Pipe(sprites, height - h - GAP, True))

    sprites.draw(screen)
    font.render_to(screen, (10, 10), f'Score: {score}', (200, 200, 200))

    c += 1
    pygame.display.flip()

pygame.quit()
