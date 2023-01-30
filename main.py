import pygame
import math

pygame.init()

Width, Height = 1000, 800
Bg_color = (205, 105, 0)
YELLOW = (255, 255, 0)
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Solar system simulation")


class Planet:
    AU = 149.6e6 * 1000  # astronomical unit
    G = 6.67e-11
    SCALE = 250 / AU
    TIMESTEP = 24*60*60  # 1 day

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

    def draw(self, win):
        x = self.x * self.SCALE + Width/2
        y = self.y * self.SCALE + Height/2
        pygame.draw.circle(win, self.color, (x, y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()

    # Create the sun
    sun = Planet(0, 0, 35, YELLOW, 1.9891 * 10**30)
    sun.sun = True

    solarSystem = [sun]

    while run:
        # Set framerate
        clock.tick(60)

        # Set Background color
        # Window.fill(Bg_color)

        # Get event that are occurring in pygame
        for event in pygame.event.get():
            # If hit X button in the window
            if event.type == pygame.QUIT:
                run = False

        for planet in solarSystem:
            planet.draw(Window)

        pygame.display.update()

    pygame.quit()


main()
