import pygame
import random
import time

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
displaywidth = 600
displayheight = 400
display = pygame.display.set_mode((displaywidth, displayheight))
pygame.display.set_caption("Snake Game ")
clock = pygame.time.Clock()
snakeblock = 10
snakespeed = 5
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def score1(score):
    value = score_font.render("Your Score : " + str(score), True, yellow)
    display.blit(value, [0, 0])


def message(msg):
    mesg = font_style.render(msg, True, black)
    display.blit(mesg, [300, 200])


def drawsnake(a, b):
    for x in b:
        pygame.draw.rect(display, black, [x[0], x[1], a, a])


def gameloop():
    gameover = False
    gameclose = False
    lengthofsnake = 1
    x1 = 300
    y1 = 200
    x1change = 0
    y1change = 0
    snakelist = []
    foodx = int(round(random.randrange(0, displaywidth - 10) / 10.0) * 10.0)
    foody = int(round(random.randrange(0, displayheight - 10) / 10.0) * 10.0)

    while not gameover:
        while gameclose == True:
            display.fill(blue)
            message("You Lost. Press C to play again or Q to quit.")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                    gameclose = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1change = -10
                    y1change = 0
                if event.key == pygame.K_RIGHT:
                    x1change = +10
                    y1change = 0
                if event.key == pygame.K_UP:
                    x1change = 0
                    y1change = -10
                if event.key == pygame.K_DOWN:
                    x1change = 0
                    y1change = +10

        x1 = x1 + x1change
        y1 = y1 + y1change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, 10, 10])
        snakehead = []
        snakehead.append(x1)
        snakehead.append(y1)
        snakelist.append(snakehead)

        if len(snakelist) > lengthofsnake:
            del snakelist[0]

        for x in snakelist[:-1]:
            if x == snakehead:
                gameclose = True

        drawsnake(10, snakelist)
        score1(lengthofsnake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randrange(0, displaywidth - 10) / 10.0) * 10.0)
            foody = int(round(random.randrange(0, displayheight - 10) / 10.0) * 10.0)
            lengthofsnake = lengthofsnake + 1

        if x1 >= displaywidth or x1 < 0 or y1 >= displayheight or y1 < 0:
            gameclose = True

        clock.tick(5)

    pygame.quit()
    quit()


gameloop()
