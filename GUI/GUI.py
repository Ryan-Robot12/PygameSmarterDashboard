from typing import Any

import pygame

blue = (0, 0, 255)
gray = (127, 127, 127)
black = (0, 0, 0)
pygame.init()
font_style = pygame.font.Font("assets/arial.ttf", 12)  # using arial.tff in case the system does not have arial for some reason


class ValueBox:
    def __init__(self, x: int, y: int, width: int = 100, height: int = 150, title: str = "", value: Any = 0):
        """
        A class that handles the GUI part of the dashboard. x/y/width/height arguments are in pixels

        :param x: x position (left = 0)
        :param y: y position (bottom = 0), modified from pygame default of top = 0
        :param width: width in pixels
        :param height: height in pixels
        :param title: title of the values
        :param value: the value to be displayed
        """
        self.x = x
        self.y = pygame.display.get_window_size()[1] - y
        self.nonOffsetY = y
        self.width = width
        self.height = height
        self.title = title
        self.value = value
        self.hasMoved = False
        self.oldX = x
        self.oldY = y

    def updatePos(self, x: int, y: int):
        """
        Updates position of the value

        :param x: x position (left = 0)
        :param y: y position (bottom = 0)
        """
        self.oldX = self.x
        self.oldY = self.y
        self.x = x
        self.y = y
        self.nonOffsetY = y
        self.hasMoved = True

    def updateValue(self, value: Any):
        self.value = value

    def updateName(self, title: str):
        self.title = title

    def getRectangle(self):
        return [self.x, self.y, self.width, self.height]

    def draw(self, display: pygame.display):
        # ignore this code if you are reading to see the good code syntax
        if self.hasMoved:
            pygame.draw.rect(display, black, [self.oldX, self.oldY, self.width, self.height])
            self.hasMoved = False

        # top blue section:
        pygame.draw.rect(display, blue, [self.x, self.y, self.width, int(self.height / 4)])
        # bottom gray section:
        pygame.draw.rect(display, gray, [self.x, self.y + int(self.height / 4), self.width, int(3 * (self.height / 4))])

        # title/value name:
        text = font_style.render(self.title, True, black)
        textRect = text.get_rect()
        textRect.center = (int(self.x + (self.width / 2)), int(self.y + (self.height / 8)))  # divide height by 8 because center of blue section is 1/4 of size, and center of that is 1/2 * 1/4 = 1/8
        display.blit(text, textRect)

        # value:
        text = font_style.render(str(self.value), True, black)
        textRect = text.get_rect()
        textRect.center = (int(self.x + (self.width / 2)), int(self.y + (self.height / (5/3))))
        display.blit(text, textRect)
        pygame.display.update()
