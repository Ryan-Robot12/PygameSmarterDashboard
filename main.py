import time

import pygame
from networktables import *
from GUI.GUI import *
from Math import *
import json

boxes = []

ip = "roborio-4829-frc.local"
NetworkTables.initialize(server=ip)
i = 0


def updateNetworkTables(display: pygame.display):
    file = json.load(open("assets/config.json"))
    global i
    for index, value in enumerate(file["values"]):
        try:
            # boxes[index].updateValue(NetworkTables.getTable(value["table"]).getValue(value["name"], "Not found"))
            if i <= 5:
                i += 1
                boxes[index].updateValue(i)
                boxes[index].draw(display)
            else:
                i = 0
        except Exception as e:
            print(e)


def main():
    global boxes

    pygame.init()
    dis = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("SmarterDashboard?")
    icon = pygame.image.load("assets/4829logo.jpg")
    pygame.display.set_icon(icon)
    pygame.display.update()

    quit_ = False

    box = ValueBox(50, 200, title="Example", value=123)
    box.draw(dis)
    boxes.append(box)
    pygame.display.update()

    dragging = False
    rightClickMenu = Menu(["Item 1", "Item 2", "Item 3", "Item 421", "item 1247"])
    showing_menu = False
    hidOnce = False

    while not quit_:
        # updateNetworkTables(dis)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_ = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging = event.button == 1 and isCoordinateInRectangle(box.getRectangle(), pygame.mouse.get_pos())

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = not event.button

            if dragging:
                box.updatePos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                box.draw(dis)

        if pygame.mouse.get_pressed(3)[2]:
            if showing_menu:
                showing_menu = False
                hidOnce = False
            else:
                showing_menu = True
                rightClickMenu.setPos(pygame.mouse.get_pos())
        if showing_menu:
            rightClickMenu.show(dis)
        else:
            if not hidOnce:
                rightClickMenu.hide(dis)
                hidOnce = True

    pygame.quit()
    quit()


main()
