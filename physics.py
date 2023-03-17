import pygame, math, random, threading
from pygame.locals import *

class Circle:
    def __init__(self, colour, radius, mass, position, velocity, rotation, rotationalVelocity, isStatic = False):
        self.colour = colour
        self.radius = radius
        self.radius = mass
        self.position = position
        self.velocity = velocity
        self.rotation = rotation
        self.rotationalVelocity = rotationalVelocity
        self.isStatic = isStatic

class Box:
    def __init__(self, colour, length, width, mass, position, velocity, rotation, rotationalVelocity, isStatic = False):
        self.colour = colour
        self.length = length
        self.width = width
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.rotation = rotation
        self.rotationalVelocity = rotationalVelocity
        self.isStatic = isStatic

width = 800
height = 450

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Physics")

clock = pygame.time.Clock()
gameExit = False

fps = 1000.0
objects = []

objects.append(Circle())
objects.append(Circle())
objects.append(Circle())
objects.append(Box())
objects.append(Box())
objects.append(Box())

gravityX = 0.0
gravityY = -1000.0

friction = 2

screenColour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

while not gameExit:
    screen.fill(screenColour)
    i = 0
    for object in objects:
        if object.position[0] + object.radius > width:
            if object.velocity[0] > 0:
                object.velocity[0] *= -1
        if object.position[0] - object.radius < 0:
            if object.velocity[0] < 0:
                object.velocity[0] *= -1
        if object.position[1] + object.radius > height:
            if object.velocity[1] > 0:
                object.velocity[1] *= -1
        if object.position[1] - object.radius < 0:
            if object.velocity[1] < 0:
                object.velocity[1] *= -1
        j = 0
        for otherObject in objects:
            if i != j:
                if ((object.position[0] - otherObject.position[0])**2)+((object.position[1] - otherObject.position[1])**2) < ((object.radius + otherObject.radius) ** 2):
                    nX = object.position[0] - otherObject.position[0]
                    nY = object.position[1] - otherObject.position[1]

                    object.velocity[0] = nX * 10
                    object.velocity[1] = nY * 10
            j += 1

        object.velocity[0] += gravityX/fps
        object.velocity[1] += gravityY/fps

        object.position[0] += object.velocity[0]/fps
        object.position[1] += object.velocity[1]/fps

        pygame.draw.circle(screen, object.colour, (int(object.position[0]), int(450 - object.position[1])), int(object.radius), 0)
        i += 1

    pygame.display.update()

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

pygame.quit()
quit()
