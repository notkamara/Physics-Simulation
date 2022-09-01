import pygame, math, threading
from pygame.locals import *

width = 800
height = 450

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Physics")

clock = pygame.time.Clock()
gameExit = False

fps = 60.0

colour = (255,0,0)
colour2 = (0,255,0)

circleX = 200.0
circleY = 225.0
circleVX = 100.0
circleVY = 0.0
circleRad = 80.0

circle2X = 720.0
circle2Y = 225.0
circle2VX = -100.0
circle2VY = 0.0
circle2Rad = 80.0

gravityX = 0.0
gravityY = -600.0

nX = 0.0
nY = 0.0

nX2 = 0.0
nY2 = 0.0

##circleV = 0
##circleRot = 0
##circleVRot = 0

bounceVX = 0.0
bounceVY = 0.0

bounce2VX = 0.0
bounce2VY = 0.0

def render():
    screen.fill((0,0,0))
    
    circlePos = (int(circleX), int(450 - circleY))
    pygame.draw.circle(screen, colour, circlePos, int(circleRad), 1)
    
    circlePos = (int(circle2X), int(450 - circle2Y))
    pygame.draw.circle(screen, colour2, circlePos, int(circle2Rad), 1)
    
    pygame.display.update()

while not gameExit:
    render()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

###############################################

    bounceVX = circleVX
    bounceVY = circleVY

    circleVX += gravityX/fps
    circleVY += gravityY/fps

    if circleX + circleRad > 800:
        circleVX = -bounceVX
    if circleX - circleRad < 0:
        circleVX = -bounceVX
    if circleY + circleRad > 450:
        circleVY = -bounceVY
    if circleY - circleRad < 0:
        circleVY = -bounceVY

##    if ((circleX - circle2X)**2)+((circleY - circle2Y)**2) < ((circleRad + circle2Rad) ** 2):
##        nX = (circleX - circle2X)/math.sqrt((circleX - circle2X)**2)+((circleY - circle2Y)**2)
##        nY = (circleY - circle2Y)/math.sqrt((circleX - circle2X)**2)+((circleY - circle2Y)**2)
##        
##        circleVX = circleVX - (2 * ((circleVX * nX) + (circleVY * nY)) * nX)

    circleX += circleVX/fps
    circleY += circleVY/fps

################################################

    bounce2VX = circle2VX
    bounce2VY = circle2VY

    circle2VX += gravityX/fps
    circle2VY += gravityY/fps

    if circle2X + circle2Rad > 800:
        circle2VX = -bounce2VX
    if circle2X - circle2Rad < 0:
        circle2VX = -bounce2VX
    if circle2Y + circle2Rad > 450:
        circle2VY = -bounce2VY
    if circle2Y - circle2Rad < 0:
        circle2VY = -bounce2VY

    if ((circleX - circle2X)**2)+((circleY - circle2Y)**2) < ((circleRad + circle2Rad) ** 2):
        n2X = ((circle2X - circleX)/math.sqrt((circleX - circle2X)**2)+((circleY - circle2Y)**2))
        n2Y = ((circle2Y - circleY)/math.sqrt((circleX - circle2X)**2)+((circleY - circle2Y)**2))
        
        circle2VX = circle2VX - (2 * ((circle2VX * n2X) + (circle2VY * n2Y)) * n2X)
        
    circle2X += circle2VX/fps
    circle2Y += circle2VY/fps

pygame.quit()
quit()
