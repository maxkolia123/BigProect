#Создай собственный Шутер!

from pygame import *
from random import randint
#Размеры окна
windowns_height = 500
windowns_width = 700
#Програма
window=display.set_mode((windowns_width, windowns_height ))
display.set_caption('shyter')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
#Запуск програмы
game = True
clock = time.Clock()
#FPS
FPS=60
lost = 0
score = 0
HP = 3
#Музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire_sound = mixer.Sound('fire.ogg')

Dead_sound = mixer.Sound('Enemy_dead.ogg')


#Шрифты
font.init()
font2 = font.SysFont('Arial', 36)
font3 = font.SysFont('Arial', 50)

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect= self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5 :
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
    def fire(self):
        bullet= Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)





   
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>=500:
            self.rect.y=0
            self.rect.x=randint(0, 600) 
                
            lost += 1 

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
            

        






player =  Player('rocket.png', 300, 400, 60, 100, 13)

bullets= sprite.Group()
final = True

enemys = sprite.Group()
for i in range(7):
	enemy = Enemy('ufo.png', randint(0, 600),0, 100, 60, randint(1, 4))
	enemy.add(enemys)


while game:
    for e  in event.get():
        if e.type == QUIT:
            game= False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                fire_sound.play()

    
    if final == True:
        window.blit(background,(0,0))
        player.update()
        player.reset()	
        text=font2.render("Счет:"+ str(score), 1, (255,255,255))
        window.blit(text, (10,20))
        text_lose = font2.render("Пропущенно:"+ str(lost), 1, (255,255,255))
        window.blit(text_lose, (10,50))
        text_hp = font2.render("Здоровье"+ str(HP), 1, (255,255,255))
        window.blit(text_hp, (10,100))
        bullets.update()
        bullets.draw(window)

        collides = sprite.groupcollide(enemys, bullets, True, True)

        if sprite.spritecollide(player, enemys, False):
            sprite.spritecollide(player, enemys, True)
            enemy = Enemy('ufo.png', randint(0, 600),0, 100, 60, randint(1, 4))
            enemy.add(enemys)
            HP -= 1
            

        if HP <= 0:
            text_lost = font3.render("Следи за здоровьем", 15, (255,255,255))
            window.blit(text_lost, (275,175)) 
            final = False





        for c in collides:
            score += 1
            Dead_sound.play()
            enemy = Enemy('ufo.png', randint(0, 600),0, 100, 60, randint(1, 4))
            enemy.add(enemys)









        for ufo in enemys:
	        ufo.reset()
	        ufo.update()


    if lost >= 11:
        text_lost = font3.render("Проиграл", 15, (255,255,255))
        window.blit(text_lost, (275,175))
        final = False
        
        

    if score >= 11:
        text_win = font3.render("Выиграл", 15, (255,255,255))
        window.blit(text_win, (275,175))
        final = False


    clock.tick(FPS)
    display.update()






