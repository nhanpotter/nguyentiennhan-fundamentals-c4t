import pygame
import sys
import random
import time
import cv2
import numpy as np
import newWebcam
# music
def play_music(x, n):
    pygame.mixer.music.load(x)
    pygame.mixer.music.play(n)

# backgrnd
my_image = pygame.image.load('D:\\project_final\\galaxy.jpg')
ship_img = pygame.image.load('D:\\project_final\\trym.png')
ship_img = pygame.transform.scale(ship_img,(30,40))
bullet_img = pygame.image.load('D:\\project_final\\sperm.png')
bullet_img = pygame.transform.scale(bullet_img,(10,20))
#
WIDTH = 400
HEIGHT = 600
FPS = 30
shootdelay = 0.08
bulletspeed = -10
# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.blit(my_image, (100, 100))
pygame.display.set_caption("Space shooting")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship_img
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT -20)
        self.lastshot = 0
    def update(self):
        if self.rect.x <0:
            self.rect.x = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        # elif self.rect.



    def shoot(self):
        self.bullet = Bullet(self.rect.centerx, self.rect.top)
        if time.time()-self.lastshot > shootdelay:
            self.lastshot = time.time()
            all_sprites.add(self.bullet)
            bullets.add(self.bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40,step=10)
        self.speedy = random.randrange(5,10,step=5)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < 0 or self.rect.right > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = bulletspeed
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.kill()
class ScoreBoard():
    def __init__(self, font_size=20, score=0):
        self.x = WIDTH - 150
        self.y = 20
        self.score = score
        self.font = pygame.font.Font('freesansbold.ttf', font_size)

    def display(self, score):
        result_srf = self.font.render('Score : %s' % score, True, WHITE)
        result_rect = result_srf.get_rect()
        result_rect.topleft = (WIDTH - 150, 20)
        screen.blit(result_srf, result_rect.topleft)

all_sprites = pygame.sprite.Group()
player = Player()
score = ScoreBoard()
enemy = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(player)
for i in range(10):
    evil = Enemy()
    all_sprites.add(evil)
    enemy.add(evil)




intro = True
running = True
c = -1

# intro and retry

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

def play():
    global intro
    intro = False

def quit():
    global intro,running
    intro = False
    running = False

def intro():
    global intro,running

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        screen.blit(my_image,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Space shooter", largeText)
        TextRect.center = ((WIDTH / 2), (HEIGHT / 2))
        screen.blit(TextSurf, TextRect)

        button("GO!",40, 530, 60, 40,green,bright_green, play)
        button("QUIT", 150, 530, 60, 40, red, bright_red,quit)
        # button("ABOUT",40,330,60,40, green,green, about)



        pygame.display.update()
        clock.tick(15)


def retry():
    global running, intro,x
    running = True
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects(x, largeText)
        TextSurf1, TextRect1 = text_objects("Your score :", largeText)
        TextRect1.center = ((WIDTH/2), (HEIGHT / 2))
        TextRect.center = ((WIDTH/2), (HEIGHT /1.75))
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1, TextRect1)

        # button("CONTINUE", 40, 530, 65, 40, green, bright_green, again)
        button("QUIT", 150, 530, 65, 40, red, bright_red, quit)

        pygame.display.update()

def again():
    global running
    running = True
    gameloop()


# gameloop

#


def gameloop():
    global score,running,c
    # keep loop running at the same speed
    vision = newWebcam.webcam()
    vision.thread_webcam()

    posX, posY = vision.get_currentPos()
    # frame = vision.get_currentFrame()
    # print(posX,posY)

    # Process input (events)
    # posX = 50
    # posY = 50
    play_music("D:\\project_final\\launch.mp3",-1)
    while running:
        posX, posY = vision.get_currentPos()
        clock.tick(FPS)
        for event in pygame.event.get():
            # closing window
            if event.type == pygame.QUIT:
                running = False
        #     if event.type == pygame.KEYUP:
        #         c = -1
        #     if event.type == pygame.KEYDOWN:
        #         c = 1
        # keys = pygame.key.get_pressed()

        # if c == keys[pygame.K_a]:
        #     player.rect.x -= 10
        # if c == keys[pygame.K_d]:
        #     player.rect.x += 10
        # if c == keys[pygame.K_SPACE]:
        #     player.shoot()
        if vision.get_len() != 0:
            player.shoot()
        if posX != 0 and posY != 0:
            player.rect.x = 1.5 * posX -50
            player.rect.y = 1.5 * posY + 250
        # Update
        all_sprites.update()

        # hits
        hits = pygame.sprite.groupcollide(bullets, enemy, True, True)
        for hit in hits:
            play_music("D:\\project_final\\bullet.mp3",1)
            evil = Enemy()
            all_sprites.add(evil)
            enemy.add(evil)
        hitst = pygame.sprite.spritecollide(player, enemy, False)
        if hitst:
            play_music("D:\\project_final\\explosion.mp3",1)
            running = False
        # Draw / render
        screen.fill(BLACK)
        screen.blit(my_image, (0, 0))
        all_sprites.draw(screen)
        if hits: score.score += 1
        score.display(score.score)
        # *after* drawing everything, flip the display
        pygame.display.flip()

intro()
gameloop()
x = str(score.score)
retry()
pygame.quit()


















