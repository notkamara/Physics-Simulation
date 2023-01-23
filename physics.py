import pygame, math, random, threading
from pygame.locals import *

class circleObject:
    def __init__(self, colour, radius, position, velocity):
        self.colour = colour
        self.radius = radius
        self.position = position
        self.velocity = velocity

width = 800
height = 450

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Physics")

clock = pygame.time.Clock()
gameExit = False

fps = 1000.0
numCircles = 100
circles = []

for i in range(numCircles):
    circles.append(circleObject([random.randint(0,255),random.randint(0,255),random.randint(0,255)],
                                 random.randint(5,30),
                                [random.randint(50,width),random.randint(50,height)], 
                                [0,0]))

gravityX = 0.0
gravityY = -1000.0

friction = 2

screenColour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

while not gameExit:
    screen.fill(screenColour)
    i = 0
    for circle in circles:
        if circle.position[0] + circle.radius > width:
            if circle.velocity[0] > 0:
                circle.velocity[0] *= -1
        if circle.position[0] - circle.radius < 0:
            if circle.velocity[0] < 0:
                circle.velocity[0] *= -1
        if circle.position[1] + circle.radius > height:
            if circle.velocity[1] > 0:
                circle.velocity[1] *= -1
        if circle.position[1] - circle.radius < 0:
            if circle.velocity[1] < 0:
                circle.velocity[1] *= -1
        j = 0
        for otherCircle in circles:
            if i != j:
                if ((circle.position[0] - otherCircle.position[0])**2)+((circle.position[1] - otherCircle.position[1])**2) < ((circle.radius + otherCircle.radius) ** 2):
                    nX = circle.position[0] - otherCircle.position[0]
                    nY = circle.position[1] - otherCircle.position[1]

                    circle.velocity[0] = nX * 10
                    circle.velocity[1] = nY * 10
            j += 1

        circle.velocity[0] += gravityX/fps
        circle.velocity[1] += gravityY/fps

        circle.position[0] += circle.velocity[0]/fps
        circle.position[1] += circle.velocity[1]/fps

        pygame.draw.circle(screen, circle.colour, (int(circle.position[0]), int(450 - circle.position[1])), int(circle.radius), 0)
        i += 1

    pygame.display.update()

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

pygame.quit()
quit()
