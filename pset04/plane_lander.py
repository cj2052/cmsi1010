"""A animation of a plane landing, controlled by the user.

The plane begins in a flying state. The user presses the down arrow key to
start descending. When the plane is close to the ground, the user must
press the up arrow key to raise the nose, otherwise the plane will crash.
After the plane touches the ground, the user presses the down arrow key
to lower the nose. Then they must press the return key to start braking.
The plane will come to a stop. At this point, the user can press the right
arrow key to start the plane again. It will accelerate on the ground until
it is going fast enough, at which point the user presses the up arrow key
to take off. The plane will then rise to a cruising altitude and fly until
the user presses the down arrow key to start descending again.
"""

import math
from dataclasses import dataclass
import pygame
import pygame.freetype

#background constants
WIDTH, HEIGHT = 1024, 600
SKY_COLOR = (135, 240, 255)
GRASS_COLOR = (150, 50, 50)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = (0, GRASS_TOP, WIDTH, GRASS_HEIGHT)
GROUND_LEVEL = HEIGHT - (GRASS_HEIGHT // 2)
TREE_SPACING = 173

#runway constants
RUNWAY_COLOR = (200,200,200)
RUNWAY_HEIGHT = GRASS_HEIGHT // 2
RUNWAY_TOP = HEIGHT - RUNWAY_HEIGHT - (GRASS_HEIGHT // 4)
RUNWAY_RECTANGLE = (0, RUNWAY_TOP, WIDTH, RUNWAY_HEIGHT)
RUNWAY_STRIPE_LENGTH = 75
RUNWAY_STRIPE_HEIGHT = 15
RUNWAY_STRIPE_SPACING = RUNWAY_STRIPE_LENGTH * 2
RUNWAY_LIGHT_SPACING = 20
RUNWAY_LIGHT_RADIUS = 5

#plane constants
MAX_PLANE_SPEED = 23
CRUISING_ALTITUDE = 50
PLANE_COLOR = (200,200,200)

score_counter = 0

#setting up background and spaceship images
bg = pygame.image.load("space2.png")
ship = pygame.image.load("images/enterprise.png")


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")
clock = pygame.time.Clock()
font = pygame.freetype.SysFont('sans', 20)
bg = bg.convert()
bg = pygame.transform.scale(bg, screen.get_size())
ship = pygame.transform.scale(ship, (100,50))

class Plane(pygame.sprite.Sprite): #Created Plane class as a sprite to overlay an image onto the plane

    def __init__(self, x, y, state="flying", speed=MAX_PLANE_SPEED, rotation=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship
        self.rect = self.image.get_rect()
        self.state = state
        self.speed = speed
        self.rotation = rotation
        self.x = x
        self.y = y
        self.rect_center = (WIDTH // 2, self.y)

    
    def draw(self): 
        #blit image with regards to the rotation to ensure that the plane position doesn't get messed up
        rotated_image = pygame.transform.rotate(ship, self.rotation)
        new_rect = rotated_image.get_rect(center=(WIDTH // 2, self.y))
        screen.blit(rotated_image,new_rect)
        

    # The states are:
    
    # "flying"     : the plane is in the air at the cruising altitude,
    #                moving forward. The user can press the down arrow
    #                key to start descending.
    # "descending" : the plane is descending towards the ground, facing
    #                downwards. The user can press the up arrow key to
    #                raise the nose and start landing. If they raise the
    #                nose too early, the plane will start rising again.
    #                If they raise the nose too late, the plane will
    #                crash. Raising it just right will put the plane
    #                in the "landing" state.
    # "landing"    : the plane has just brought the nose up, right above
    #                the ground, and is still going down. When it hits
    #                the ground, it will be in the "touching" state.
    # "touching"   : the plane has just touched the ground, and is
    #                still moving forward with the nose up. The user
    #                can press the down arrow key to lower the nose,
    #                but it will still be moving forward fast.
    # "down"       : the user has just lowered the nose so all wheels
    #                are on the ground and the plane is moving
    #                forward. The user needs to press the Return key
    #                here to start braking.
    # "braking"    : the plane is on the ground, decelerating. When
    #                it comes to a stop, it will be in the "stopped"
    #                state.
    # "stopped"    : the plane has come to a stop on the ground.
    #                In the stopped state, the user can press the right
    #                arrow key to start the plane moving again.
    # "starting"   : the plane is starting to move on the ground, and
    #                the user can press the up arrow key to take off.
    # "rising"     : the plane is rising after touching down. It will
    #                keep rising until it reaches the cruising altitude
    #                in which case it will automatically level off and
    #                return to the "flying" state.
    # "crashed"    : the plane has crashed and is no longer moving.

    def move(self):
        if self.state != "stopped":
            self.x += self.speed % TREE_SPACING
        if self.state == "flying":
            pass
        elif self.state == "descending":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "crashed"
        elif self.state == "landing":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "touching"
                self.y = GROUND_LEVEL
        elif self.state == "touching":
            pass
        elif self.state == "down":
            pass
        elif self.state == "braking":
            self.speed -= 0.1
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"
        elif self.state == "starting":
            self.y = GROUND_LEVEL
            self.speed += 0.1
            if self.speed >= MAX_PLANE_SPEED:
                self.speed = MAX_PLANE_SPEED
        elif self.state == "rising":
            self.y -= self.speed * 0.1
            if self.y <= CRUISING_ALTITUDE:
                self.y = CRUISING_ALTITUDE
                self.state = "flying"
                self.rotation = 0
        elif self.state == "crashed":
            self.color = (255, 0, 0)  # red for crashed
            self.speed = 0
            self.y = GROUND_LEVEL
            font.render_to(screen, (WIDTH // 2, HEIGHT // 2), f"Game Over \n Press ENTER to Start Again", (255,255,255))

    def restart(self): #restard method resets the plane to its original parameters
        self.state = "flying"
        self.color = (PLANE_COLOR)
        self.y = CRUISING_ALTITUDE
        self.speed = MAX_PLANE_SPEED
        self.rotation = 0

plane = Plane(0, y=CRUISING_ALTITUDE)

def rotate(image, rect, rotation): #rotate function rotates the image when the rotation angle is adjusted
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, rotation)
        rot_rect = plane.rect_center
        return rot_image,rot_rect

def draw_runway_stripes(x, y):
    pygame.draw.rect(screen, (255,255,0), 
                     (x, y, RUNWAY_STRIPE_LENGTH, RUNWAY_STRIPE_HEIGHT))

def draw_runway_lights(x, y):
    pygame.draw.circle(screen, (255,255,255), (x, y), radius=RUNWAY_LIGHT_RADIUS)


def draw_scene():
    if plane.state != "stopped":
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)
        pygame.draw.rect(screen, RUNWAY_COLOR, RUNWAY_RECTANGLE)
        x_runway = -plane.x
        x_lights = -plane.x
        while x_runway < WIDTH:
            draw_runway_stripes(x_runway, RUNWAY_TOP + RUNWAY_STRIPE_HEIGHT)
            x_runway += RUNWAY_STRIPE_SPACING
        while x_lights < WIDTH:
            draw_runway_lights(x_lights, RUNWAY_TOP - 15)
            draw_runway_lights(x_lights, RUNWAY_TOP + RUNWAY_HEIGHT + 15)
            x_lights += RUNWAY_LIGHT_SPACING
        plane.draw()
        font.render_to(screen, (WIDTH - 100, 50), f"Score: {score_counter}", (255,255,255) ) #score counter printed here
        plane.move()
    clock.tick(60)
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and plane.state == "flying":
                plane.rotation = -20 #plane rotation angles change and then rotate() is called to set the plane to the new angle
                plane.image, plane.rect = rotate(plane.image, plane.rect, plane.rotation) 
                plane.state = "descending"
            elif event.key == pygame.K_UP and plane.state == "descending":
                plane.rotation = 20
                plane.image, plane.rect = rotate(plane.image, plane.rect, plane.rotation) 
                if plane.y < GROUND_LEVEL - 100:
                    plane.state = "rising"
                else:
                    plane.state = "landing"
            elif event.key == pygame.K_DOWN and plane.state == "touching":
                plane.rotation = 0
                plane.image, plane.rect = rotate(plane.image, plane.rect, plane.rotation)             
                plane.state = "down"
            elif event.key == pygame.K_RETURN and plane.state == "down":
                plane.state = "braking"
            elif event.key == pygame.K_RIGHT and plane.state == "stopped":
                score_counter += 1 #score counter increases when the plane reaches the stopped condition
                plane.state = "starting"
            elif event.key == pygame.K_UP and plane.state == "starting" \
                    and plane.speed == MAX_PLANE_SPEED:
                plane.rotation = 10
                plane.image, plane.rect = rotate(plane.image, plane.rect, plane.rotation) 
                plane.state = "rising"
            if event.key == pygame.K_RETURN and plane.state == "crashed":
                plane.restart() #reset method is called when the plane is crashed and the user presses enter 
                score_counter = 0 #score counter is reset when the game is restarted
    draw_scene()