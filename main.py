import pygame
from time import sleep
# from _pynetworktables import *
from NetworkTablesHandling import *
from GUI.GUI import *
from Math import *


def main():
    pygame.init()
    dis = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("SmarterDashboard?")
    icon = pygame.image.load("assets/4829logo.jpg")
    pygame.display.set_icon(icon)
    pygame.display.update()
    quit_ = False
    box = ValueBox(50, 200, title="Example", value=123)
    box.draw(dis)
    pygame.display.update()
    dragging = False
    while not quit_:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_ = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging = event.button = 1 and isCoordinateInRectangle(box.getRectangle(), pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = not event.button
            if dragging:
                box.updatePos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                box.draw(dis)
        print(dragging)
        # print(box.getRectangle())
        # print(pygame.mouse.get_pos())
        # print(isCoordinateInRectangle(box.getRectangle(), pygame.mouse.get_pos()))
        # sleep(1)

        # for i in range(10):
        #     box.updateValue(i)
        #     box.draw(dis)
        #     sleep(1)

    pygame.quit()
    quit()


main()
