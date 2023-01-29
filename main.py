import pygame
import math

pygame.init()

Width, Height = 1000, 800
Bg_color = (205, 105, 0)
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Solar system simulation")


class Planet:
    AU = 149.6e6 * 1000  # astronomical unit
    G = 6.67e-11
    SCALE = 250 / AU

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.x_velocity = 0
        self.y_velocity = 0

        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        # Set framerate
        clock.tick(60)

        # Set Background color
        # Window.fill(Bg_color)
        # pygame.display.update()

        # Get event that are occurring in pygame
        for event in pygame.event.get():
            # If hit X button in the window
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()
