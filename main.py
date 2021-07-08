import pygame
import os
from time import sleep

WIDTH, HEIGHT = 900, 500

RED_SPACESHIP = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
YELLOW_SPACESHIP = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH,HEIGHT))

pygame.font.init()

WINNER_FONT = pygame.font.SysFont('comicsans', 175)

RED = (255, 0, 0)
YELLOW = (255, 211, 67)
GREEN = (0, 255, 0)

class Spaceships:
    R_SPACESHIP = RED_SPACESHIP
    Y_SPACESHIP = YELLOW_SPACESHIP
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGTH = 55
    VEL = 1
    BULLET_VEL = 7

    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.red = pygame.transform.scale(pygame.transform.rotate(self.R_SPACESHIP, 90), (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGTH))
        self.yellow = pygame.transform.scale(pygame.transform.rotate(self.Y_SPACESHIP, -90),(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGTH))
        self.R_rect = pygame.Rect(self.x, self.y, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGTH)
        self.Y_rect = pygame.Rect(self.x2, self.y2, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGTH)
        pygame.display.init()
        self.key = pygame.key.get_pressed()
        self.red_health_width = 40
        self.yellow_health_width = 40

        self.red_bullets = []
        self.yellow_bullets = []
        self.red_bullet = pygame.Rect(self.x + self.SPACESHIP_WIDTH, self.y + self.SPACESHIP_HEIGTH//2 - 3, 10, 6)
        self.yellow_bullet = pygame.Rect(self.x2 - 10, self.y2 + self.SPACESHIP_HEIGTH // 2 - 3, 10, 6)
        self.red_health = pygame.Rect(self.x, self.y -10, self.red_health_width, 6)
        self.yellow_health = pygame.Rect(self.x2, self.y2 -10, self.yellow_health_width, 6)

        self.red_winner = WINNER_FONT.render("Red Won!!", 1, RED)
        self.yellow_winner = WINNER_FONT.render("Yellow Won!!", 1, YELLOW)

    def move_red(self):
        self.red_health
        self.R_rect = pygame.Rect(self.x, self.y, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGTH)
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_a] and self.x - self.VEL > 0:
            self.x -= self.VEL
            self.red_health.x -= self.VEL
        if self.key[pygame.K_d] and self.x + self.SPACESHIP_WIDTH + self.VEL < WIDTH//2 - 5:
            self.x += self.VEL
            self.red_health.x += self.VEL
        if self.key[pygame.K_w] and self.y - self.VEL > 0:
            self.y -= self.VEL
            self.red_health.y -= self.VEL
        if self.key[pygame.K_s] and self.y + self.SPACESHIP_HEIGTH + self.VEL < HEIGHT:
            self.y += self.VEL
            self.red_health.y += self.VEL


    def move_yellow(self):
        self.yellow_health
        self.Y_rect = pygame.Rect(self.x2, self.y2, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGTH)
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_LEFT] and self.x2 - self.VEL > WIDTH//2 + 10:
            self.x2 -= self.VEL
            self.yellow_health.x -= self.VEL
        if self.key[pygame.K_RIGHT] and self.x2 + self.SPACESHIP_WIDTH + self.VEL < WIDTH:
            self.x2 += self.VEL
            self.yellow_health.x += self.VEL
        if self.key[pygame.K_UP] and self.y2 - self.VEL > 0:
            self.y2 -= self.VEL
            self.yellow_health.y -= self.VEL
        if self.key[pygame.K_DOWN] and self.y2 + self.SPACESHIP_HEIGTH + self.VEL < HEIGHT:
            self.y2 += self.VEL
            self.yellow_health.y += self.VEL

    def shoot_bullet(self):
        self.yellow_bullet = pygame.Rect(self.x2 - 10, self.y2 + self.SPACESHIP_HEIGTH // 2 - 3, 10, 6)
        self.red_bullet = pygame.Rect(self.x + self.SPACESHIP_WIDTH, self.y + self.SPACESHIP_HEIGTH // 2 - 3, 10, 6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif self.red_health_width == 0:
                self.win.blit(self.yellow_winner, (40, 40))
                pygame.display.update()
                sleep(3)
                pygame.quit()
                quit()

            elif self.yellow_health_width == 0:
                self.win.blit(self.red_winner, (40, 40))
                pygame.display.update()
                sleep(3)
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                self.red_bullets.append(self.red_bullet)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
                self.yellow_bullets.append(self.yellow_bullet)

    def draw_red_bullets(self):
        self.red_health_width
        self.red_health = pygame.Rect(self.x, self.y -10, self.red_health_width, 6)
        for bullet in self.red_bullets:
            pygame.draw.rect(self.win, RED, bullet, 0)
            bullet.x += self.BULLET_VEL
            if self.Y_rect.colliderect(bullet):
                self.red_bullets.remove(bullet)
                self.yellow_health_width -= 4

            elif bullet.x > WIDTH:
                self.red_bullets.remove(bullet)

    def draw_yellow_bullets(self):
        self.yellow_health_width
        self.yellow_health = pygame.Rect(self.x2, self.y2 -10, self.yellow_health_width, 6)
        for bullet in self.yellow_bullets:
            pygame.draw.rect(self.win, YELLOW, bullet, 0)
            bullet.x -= self.BULLET_VEL
            if self.R_rect.colliderect(bullet):
                self.yellow_bullets.remove(bullet)
                self.red_health_width -= 4


            elif bullet.x < 0:
                self.yellow_bullets.remove(bullet)

    def draw(self):
        self.win.blit(self.red, (self.x,self.y))
        self.win.blit(self.yellow, (self.x2,self.y2))
        pygame.draw.rect(self.win, GREEN, self.red_health, 0)
        pygame.draw.rect(self.win, GREEN, self.yellow_health, 0)


class Main(Spaceships):
    def __init__(self):
        super().__init__(100, 300, 700, 300)
        self.win = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("spaceship fighter")

    def set_screen(self):
        self.win.blit(SPACE, (0,0))

    def refresh(self):
        pygame.display.update()

    def start(self):
        while True:
            self.set_screen()
            self.draw()
            self.move_red()
            self.move_yellow()
            self.shoot_bullet()
            self.draw_red_bullets()
            self.draw_yellow_bullets()
            self.refresh()

def main():
    Game = Main()
    Game.start()

if __name__ == "__main__":
    main()