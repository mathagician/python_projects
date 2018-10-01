import sys, pygame as pg
from pygame.locals import  *

import random as rdm

WIDTH_SC = 480
HEIGHT_SC = 640
class Meteor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.base_name = "sprites/meteor/meteor000"+(str(rdm.randrange(1,12)))+".png"
        self.img = pg.transform.scale(load_img(str(self.base_name), True), [90,60])
        self.rect = self.img.get_rect()
        self.rect.centerx ,self.rect.centery = rdm.randrange(0, WIDTH_SC), 1
        self.speed = 0.2

    def update(self, time):
        self.rect.centery += self.speed * time

class AirPlane(pg.sprite.Sprite):
    """docstring for AirPlane."""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.img = load_img("sprites/plane.png", True)
        self.rect = self.img.get_rect()
        self.rect.centerx, self.rect.centery = WIDTH_SC / 2, HEIGHT_SC / 2
        self.speed = [1, -1]

    def update(self, time, direction = None):
        if direction == "right":
            self.rect.centerx += self.speed[0] * time
        if direction == "left":
            self.rect.centerx -= self.speed[0] * time
        if direction == "top":
            self.rect.centery -= self.speed[0] * time
        if direction == "bottom":
            self.rect.centery += self.speed[0] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH_SC:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT_SC:
           self.speed[1] = -self.speed[1]
           self.rect.centery += self.speed[1] * time

    def check_collision(self, object):
        if pg.sprite.collide_rect(self, object):
            print("Hola")

def load_img(file, transparent = False):
    try:
        img = pg.image.load(file)
    except (pg.error, KeyError):
        raise (SystemExit, KeyError)
    img = img.convert()
    if transparent:
        color = img.get_at((0,0))
        img.set_colorkey(color, RLEACCEL)
    return img

def main():
    screen = pg.display.set_mode((WIDTH_SC, HEIGHT_SC))
    clock = pg.time.Clock()
    bg_img = load_img("sprites/sky1.png")
    plane = AirPlane()
    m = Meteor()
    meteors = []

    while True:
        time = clock.tick(60)
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    plane.update(time, "left")
                if event.key == pg.K_RIGHT:
                    plane.update(time, "right")
                if event.key == pg.K_DOWN:
                    plane.update(time, "bottom")
                if event.key == pg.K_UP:
                    plane.update(time, "top")
        plane.update(time)
        plane.check_collision(m)
        m.update(time)
        screen.blit(bg_img,(0,0))
        screen.blit(plane.img, plane.rect)
        screen.blit(m.img, m.rect)
        pg.display.flip()

if __name__ == '__main__':
    pg.init()
    main()
