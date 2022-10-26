import pygame


def isCoordinateInRectangle(rectangle, point):
    """
    Is a point in a rectangle? Well, let's find out...

    :param rectangle: tuple: [x, y, width, height]
    :param point: tuple: [x, y]
    :return: if the point is inside the rectangle
    """
    rectangle = pygame.Rect(rectangle[0], rectangle[1], rectangle[2], rectangle[3])  # please don't question this -_-
    return rectangle.collidepoint(point[0], point[1])
