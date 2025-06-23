from dataclasses import dataclass
import math
import pygame
import pygame.freetype
import random

pygame.init()
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("K'tah")
clock = pygame.time.Clock()
font = pygame.freetype.SysFont('sans', 100)
frozen = False
UNFREEZE = pygame.USEREVENT + 1
scarecrow = None
REMOVE_SCARECROW = pygame.USEREVENT + 2
min_zombie_speed = 1
max_zombie_speed = 5
num_of_zombies = 8
max_zombie_size = 25
ZOMBIE_SPEED_INCREASE = pygame.USEREVENT + 3
zombie_speed_increase_interval = 3000
zombie_speed_increase_amount = 0.1
z_speed_inc = 0
safe_zone_rect = (WIDTH // 2 ,HEIGHT // 2, 100, 100)


@dataclass
class Agent:
    x: int
    y: int
    radius: int
    speed: int
    color: tuple

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move_towards(self, target):
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = math.hypot(dx, dy)
        if distance > 3.0:
            # Allow three pixels of leeway to avoid jittering
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
    
    def is_collided_with(self, other):
        distance = math.hypot(self.x - other.x, self.y - other.y)
        return distance < (self.radius + other.radius)

    def in_safe_zone(self):
        if Agent in safe_zone_rect:
            pass #LEFT OFF HERE


@dataclass
class Player(Agent):
    x: int = WIDTH // 2
    y: int = HEIGHT // 2
    radius: int = 20
    speed: int = 5
    color: tuple = (200, 200, 255)

    def teleport(self, pos):
        self.x, self.y = pos

    def is_caught_by_any_of(self, zombies):
        for zombie in zombies:
            if self.is_collided_with(zombie):
                return True
        return False


@dataclass
class Zombie(Agent):
    speed: int = 2
    radius: int = 20
    color: tuple = (80, 255, 0)

def draw_safe_zone():
    pygame.draw.rect(screen, color = (0,255,0), rect = (WIDTH // 2 ,HEIGHT // 2,100,100))

def create_zombies():
    zombies = []
    for zombie in range(0, num_of_zombies):
        rand_x = random.randint(20, WIDTH - 20)
        rand_y = random.randint(20, HEIGHT - 20) 
        rand_speed = random.randint(min_zombie_speed, max_zombie_speed)
        rand_r = random.randint(0,256)
        rand_g = random.randint(0,256)
        rand_b = random.randint(0,256)
        rand_radius = random.randint(0, max_zombie_size)
        zombies.append(Zombie(x = rand_x, 
                              y = rand_y, 
                              speed = rand_speed, 
                              radius = rand_radius, 
                              color = (rand_r, rand_g, rand_b)))
    return zombies

player = Player()
zombies = create_zombies()

def draw_scene():
    if player.is_caught_by_any_of(zombies):
        font.render_to(screen, (100, 100), "GAME OVER", (255, 0, 0))
        z_speed_inc = 0
        pygame.display.flip()
        return
    if player.is_caught_by_any_of(zombies):
        return    
    player.move_towards(pygame.mouse.get_pos())
    for zombie in zombies:
        if not frozen:
            target = scarecrow or (player.x, player.y)
            zombie.move_towards(target)
    screen.fill((0, 100, 0))
    draw_safe_zone()
    player.draw()
    for zombie in zombies:
        zombie.draw()
    if scarecrow is not None:
        pygame.draw.circle(screen, (255, 200, 0), scarecrow, 20)    
    clock.tick(60)
    pygame.display.flip()


pygame.time.set_timer(ZOMBIE_SPEED_INCREASE, zombie_speed_increase_interval)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.teleport(event.pos) 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if not frozen:
                    frozen = True
                    pygame.time.set_timer(UNFREEZE, 5000, loops=1)
            elif event.key == pygame.K_s:
                if scarecrow is None:
                    scarecrow = (player.x, player.y)
                    pygame.time.set_timer(REMOVE_SCARECROW, 5000, loops=1)
        elif event.type == UNFREEZE:
            frozen = False  
        elif event.type == REMOVE_SCARECROW:
            scarecrow = None   
        elif event.type == ZOMBIE_SPEED_INCREASE:
            for zombie in zombies:
                z_speed_inc += zombie_speed_increase_amount  
                zombie.speed * z_speed_inc       
    clock.tick(60)
    draw_scene()