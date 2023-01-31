import pygame
import math

pygame.init()

Width, Height = 1200, 800
Bg_color = (205, 105, 0)

DARKORANGE = (255, 140, 0)
MEDIUMBLUE = (0, 0, 205)
DARKGRAY = (169, 169, 169)
BROWN = (120, 42, 42)
RED = (188, 39, 50)
GOLDENROD = (218, 165, 32)
MEDIUMPURPLE = (147, 112, 219)
LIGHTBLUE = (173, 216, 230)
DODGERBLUE = (30, 144, 255)

Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Solar system simulation")


class Planet:
    AU = 149.6e6 * 1000  # astronomical unit
    G = 6.67e-11
    SCALE = 200 / AU
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
    sun = Planet(0, 0, 40, DARKORANGE, 1.9891 * 10**30)
    sun.sun = True

    # Create planets
    mercury = Planet(-0.35 * Planet.AU, 0, 9, DARKGRAY, 0.33 * 10**24)
    venus = Planet(-0.6 * Planet.AU, 0, 15, BROWN, 4.87 * 10**24)
    earth = Planet(-0.8 * Planet.AU, 0, 16, MEDIUMBLUE, 5.97 * 10**24)
    mars = Planet(-1 * Planet.AU, 0, 12, RED, 0.64 * 10**24)
    jupiter = Planet(-1.25 * Planet.AU, 0, 20, GOLDENROD, 1.8986 * 10**27)
    saturn = Planet(-1.5 * Planet.AU, 0, 18, MEDIUMPURPLE, 5.6846 * 10**26)
    uranus = Planet(-1.75 * Planet.AU, 0, 17, LIGHTBLUE, 8.662 * 10**25)
    neptune = Planet(-2 * Planet.AU, 0, 17, DODGERBLUE, 1.0243 * 10**26)


    solarSystem = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

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
