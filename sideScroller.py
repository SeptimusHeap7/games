import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images', 'C:\\Users\\rgandhi\\3D Objects\\bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()
# "C:\\Users\\rgandhi\\3D Objects\\8.png"
# "C:\\Users\\rgandhi\\3D Objects\\S2.png"

class player(object):
    run = [pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', str(x) + '.png')) for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S1.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S2.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S3.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S4.png')),
             pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', 'S5.png'))]
    fall = pygame.image.load(os.path.join('C:\\Users\\rgandhi\\3D Objects\\', '0.png'))
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
        self.falling = False

    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))

        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x, self.y + 3, self.width - 8, self.height - 35)

            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
                self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
            win.blit(self.slide[self.slideCount // 10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount // 6], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 13)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class saw(object):
    img = [pygame.image.load(os.path.join('images', 'C:\\Users\\rgandhi\\3D Objects\\SAW0.png')),
           pygame.image.load(os.path.join('images', 'C:\\Users\\rgandhi\\3D Objects\\SAW1.png')),
           pygame.image.load(os.path.join('images', 'C:\\Users\\rgandhi\\3D Objects\\SAW2.png')),
           pygame.image.load(os.path.join('images', 'C:\\Users\\rgandhi\\3D Objects\\SAW3.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0

    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        if self.count >= 8:
            self.count = 0
        win.blit(pygame.transform.scale(self.img[self.count//2], (64, 64)), (self.x, self.y))
        self.count += 1
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


class spike(saw):
    img = pygame.image.load(os.path.join('images', 'C:\\Users\\rgandhi\\3D Objects\\spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28, 315)
        win.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False


def updateFile():
    f = open('C:\\Rishi\\prj\\python\\score.txt.txt', 'r')
    file = f.readlines()
    last = int(file[0])
    if last < int(score):
        f.close()
        file = open('C:\\Rishi\\prj\\python\\score.txt.txt', 'w')
        file.write(str(score))
        file.close()
        return score
    return last

def endScreen():
    global pause, objects, speed, score
    pause = 0
    objects = []
    speed = 60

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        win.blit(bg, (0, 0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        previousScore = largeFont.render('Previous Score:' + str(updateFile()), 1, (255, 255, 255))
        win.blit(previousScore, (W / 2 - previousScore.get_width() / 2, 200))
        newScore = largeFont.render('Score:' + str(score), 1, (255, 255, 255))
        win.blit(newScore, (W / 2 - newScore.get_width() / 2, 320))
        pygame.display.update()
    score = 0
    runner.falling = False


runner = player(200, 313, 64, 64)
pygame.time.set_timer(USEREVENT + 1, 500)
pygame.time.set_timer(USEREVENT + 2, random.randrange(3000, 5000))
speed = 30
run = True

global pause, fallspeed
pause = 0
fallspeed = 0
objects = []

while run:
    score = speed//5 - 6
    def redrawWindow():
        global pause, fallspeed
        if pause > 0:
            pause += 1
            if pause > fallspeed * 2:
                endScreen()
        for objectt in objects:
            if objectt.collide(runner.hitbox):
                runner.falling = True
                if pause == 0:
                    fallspeed = speed
                    pause = 1

            objectt.x -= 1.4
            if objectt.x < objectt.width * -1:
                objects.pop(objects.index(objectt))
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
        runner.draw(win)
        for x in objects:
            x.draw(win)
        font = pygame.font.SysFont('times new roman', 30)
        text = font.render('Score:' + str(score), 1, (255, 255, 255))
        win.blit(text, (700, 10))

        pygame.display.update()
    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == USEREVENT + 1:
            speed += 1

        if event.type == USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0:
                objects.append(saw(810, 310, 64, 64))
            else:
                objects.append(spike(810, 0, 48, 320))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not runner.jumping:
            runner.jumping = True

    if keys[pygame.K_DOWN]:
        if not runner.sliding:
            runner.sliding = True

    clock.tick(speed)
    redrawWindow()
