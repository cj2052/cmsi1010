import pygame
from dataclasses import dataclass

WIDTH, HEIGHT = 800, 600
SKY_COLOR = (0, 0, 0)
SUN_COLOR = (200, 200, 200)
SUN_POSITION = (WIDTH - 100, 100)
SUN_RADIUS = 150
GRASS_COLOR = (0, 20, 0)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = (0, GRASS_TOP, WIDTH, GRASS_HEIGHT)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()

@dataclass
class UFO:
    x:int
    y:int
    width:int = 100
    height:int = 30
    color: tuple = (128,128,128)
    beam_color: tuple = (0,0,255)
    speed: int = 1

    def draw(self):
        pygame.draw.polygon(
            screen, self.beam_color, 
            ((self.x + self.width//4, self.y - self.height//3), (self.x + (3 * (self.width//4)), self.y - self.height//3),
            (self.x + self.width //2 + 50, self.y + (HEIGHT - self.x)),
            (self.x - 50, self.y + (HEIGHT - self.x))))
        pygame.draw.ellipse(
            screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(
            screen, self.color,
            (self.x + self.width//4, self.y-self.height//3, self.width//2, self.height))
        
    
    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -self.width

@dataclass
class Star:
    x:int
    y:int
    width:int=5
    height:int=5
    color:tuple = (255, 255, 0)

    def draw(self):
        pygame.draw.polygon(
            screen, self.color, 
            ((self.x, self.y), (self.x + self.width //2, self.y + self.height//2),
              (self.x + self.width, self.y), (self.x + self.width//2, self.y - self.height//2)))

ufos = [
    UFO(x=0, y=50),
    UFO(x=200, y=100, width=80, height=20, speed=3.5),
    UFO(x=400, y=150, width=120, speed=3),
    UFO(x=600, y=200, color=pygame.Color("purple"), speed=4),
    UFO(x=250, y= 50, speed= 0.5, color = pygame.Color("red")), 
    UFO(x = 10, y = 20, height = 1, width = 1, speed = 10),
    UFO(x = 650, y = 500, height = 80, width = 210, color = pygame.Color("green"))
]

stars = [
    
    Star(x = 20, y = 20), 
    Star(x = 400, y = 100)

]

def draw_scene():
    screen.fill(SKY_COLOR)
    pygame.draw.circle(screen, SUN_COLOR, SUN_POSITION, SUN_RADIUS)
    pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)
    for ufo in ufos:
        ufo.draw()
        ufo.move()
    for star in stars:
        star.draw()
    pygame.display.flip()
    clock.tick(60)


draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
    draw_scene()