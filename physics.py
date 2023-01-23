import pygame, math, threading
from pygame.locals import *

width = 800
height = 450

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Physics")

clock = pygame.time.Clock()
gameExit = False

fps = 120.0

colour = (255,0,0)
colour2 = (0,255,0)
colour3 = (0,0,255)

circleX = 200.0
circleY = 225.0
circleVX = 100.0
circleVY = 0.0
circleRad = 80.0

circle2X = 720.0
circle2Y = 225.0
circle2VX = -300.0
circle2VY = 500.0
circle2Rad = 20.0

circle3X = 520.0
circle3Y = 225.0
circle3VX = -250.0
circle3VY = 450.0
circle3Rad = 50.0

gravityX = 0.0
gravityY = -100.0

nX = 0.0
nY = 0.0

screen.fill((0,0,0))

pygame.draw.circle(screen, colour, (int(circleX), int(450 - circleY)), int(circleRad), 1)
pygame.draw.circle(screen, colour2, (int(circle2X), int(450 - circle2Y)), int(circle2Rad), 1)
pygame.draw.circle(screen, colour3, (int(circle3X), int(450 - circle3Y)), int(circle3Rad), 1)

pygame.display.update()

while not gameExit:

    if circleX + circleRad > width:
      if circleVX > 0:
        circleVX *= -1
    if circleX - circleRad < 0:
      if circleVX < 0:
        circleVX *= -1
    if circleY + circleRad > height:
      if circleVY > 0:
        circleVY *= -1
    if circleY - circleRad < 0:
      if circleVY < 0:
        circleVY *= -1

    if circle2X + circle2Rad > width:
      if circle2VX > 0:
        circle2VX *= -1
    if circle2X - circle2Rad < 0:
      if circle2VX < 0:
        circle2VX *= -1
    if circle2Y + circle2Rad > height:
      if circle2VY > 0:
        circle2VY *= -1
    if circle2Y - circle2Rad < 0:
      if circle2VY < 0:
        circle2VY *= -1

    if circle3X + circle3Rad > width:
      if circle3VX > 0:
        circle3VX *= -1
    if circle3X - circle3Rad < 0:
      if circle3VX < 0:
        circle3VX *= -1
    if circle3Y + circle3Rad > height:
      if circle3VY > 0:
        circle3VY *= -1
    if circle3Y - circle3Rad < 0:
      if circle3VY < 0:
        circle3VY *= -1

    if ((circleX - circle2X)**2)+((circleY - circle2Y)**2) < ((circleRad + circle2Rad) ** 2):
        nX = circleX - circle2X
        nY = circleY - circle2Y

        circleVX += nX
        circleVY += nY

        circle2VX -= nX
        circle2VY -= nY

    if ((circle2X - circle3X)**2)+((circle2Y - circle3Y)**2) < ((circle2Rad + circle3Rad) ** 2):
        nX = circle2X - circle3X
        nY = circle2Y - circle3Y

        circle2VX += nX
        circle2VY += nY

        circle3VX -= nX
        circle3VY -= nY

    if ((circleX - circle3X)**2)+((circleY - circle3Y)**2) < ((circleRad + circle3Rad) ** 2):
        nX = circleX - circle3X
        nY = circleY - circle3Y

        circleVX += nX
        circleVY += nY

        circle3VX -= nX
        circle3VY -= nY

    circleVX += gravityX/fps
    circleVY += gravityY/fps

    circleX += circleVX/fps
    circleY += circleVY/fps
    
    circle2VX += gravityX/fps
    circle2VY += gravityY/fps
        
    circle2X += circle2VX/fps
    circle2Y += circle2VY/fps

    circle3VX += gravityX/fps
    circle3VY += gravityY/fps
        
    circle3X += circle3VX/fps
    circle3Y += circle3VY/fps

    print(circle3VY)

    screen.fill((0,0,0))

    pygame.draw.circle(screen, colour, (int(circleX), int(450 - circleY)), int(circleRad), 0)
    pygame.draw.circle(screen, colour2, (int(circle2X), int(450 - circle2Y)), int(circle2Rad), 0)
    pygame.draw.circle(screen, colour3, (int(circle3X), int(450 - circle3Y)), int(circle3Rad), 0)

    pygame.display.update()

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

pygame.quit()
quit()
