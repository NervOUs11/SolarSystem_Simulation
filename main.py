import pygame
import math

pygame.init()

Width, Height = 1200, 800
Bg_color = (0, 0, 0)

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
    SCALE = 190 / AU  # convert real scale to simulation scale
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
        # use Width/2 and Height/2 to draw planets at the center of the screen
        x = self.x * self.SCALE + Width/2
        y = self.y * self.SCALE + Height/2

        # draw lines
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + Width/2
                y = y * self.SCALE + Height/2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt((distance_x ** 2) + (distance_y ** 2))

        # if other is the sun
        if other.sun:
            self.distance_to_sun = distance

        force = (self.G * self.mass * other.mass) / distance**2

        # break down force into x and y
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        totalForce_x = 0
        totalForce_y = 0

        # calculate all forces from other planets acting on this planet
        for planet in planets:
            # don't calculate the force you exert on yourself
            if self == planet:
                continue

            force_x, force_y = self.attraction(planet)
            totalForce_x += force_x
            totalForce_y += force_y

        # Physic ----> F = ma ----> a = F / m
        # increase velocity by acceleration * TIMESTEP
        self.x_velocity += (totalForce_x / self.mass) * self.TIMESTEP
        self.y_velocity += (totalForce_y / self.mass) * self.TIMESTEP

        # change position (x and y)
        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    # Create the sun
    sun = Planet(0, 0, 35, DARKORANGE, 1.9891 * 10**30)
    sun.sun = True

    # Create planets
    mercury = Planet(-0.35 * Planet.AU, 0, 9, DARKGRAY, 0.33 * 10**24)
    mercury.y_velocity = 47.9 * 1000

    venus = Planet(0.7 * Planet.AU, 0, 15, BROWN, 4.87 * 10**24)
    venus.y_velocity = 35 * 1000

    earth = Planet(-1.05 * Planet.AU, 0, 16, MEDIUMBLUE, 5.97 * 10**24)
    earth.y_velocity = 29.8 * 1000

    mars = Planet(1.4 * Planet.AU, 0, 12, RED, 0.64 * 10**24)
    mars.y_velocity = 24.1 * 1000

    jupiter = Planet(-1.75 * Planet.AU, 0, 20, GOLDENROD, 1.8986 * 10**27)
    jupiter.y_velocity = 13.1 * 1000

    saturn = Planet(2.1 * Planet.AU, 0, 18, MEDIUMPURPLE, 5.6846 * 10**26)
    saturn.y_velocity = 9.7 * 1000

    uranus = Planet(-2.45 * Planet.AU, 0, 17, LIGHTBLUE, 8.662 * 10**25)
    uranus.y_velocity = 6.8 * 1000

    neptune = Planet(2.8 * Planet.AU, 0, 17, DODGERBLUE, 1.0243 * 10**26)
    neptune.y_velocity = 5.4 * 1000


    # solarSystem = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    solarSystem = [sun, mercury, venus, earth, mars]

    while run:
        # Set framerate
        clock.tick(60)

        # Set Background color
        Window.fill(Bg_color)

        # Get event that are occurring in pygame
        for event in pygame.event.get():
            # If hit X button in the window
            if event.type == pygame.QUIT:
                run = False

        for planet in solarSystem:
            planet.update_position(solarSystem)
            planet.draw(Window)

        pygame.display.update()

    pygame.quit()


main()