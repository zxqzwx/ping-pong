from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Ping_pong")
back = (200, 200, 255)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700 - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700 - 80:
            self.rect.y += self.speed

racket_1 = Player('racket_l.png', 5, 200, 10, 50, 5)
racket_2 = Player('racket_r.png', 690, 200, 10, 50, 5)
ball = GameSprite('ball.png', 200, 200, 50, 50, 10)

speed_y = 3
speed_x = 3
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False


    if not finish:
        window.fill(back)
        racket_1.update_l()
        racket_2.update_r()

        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket_1.reset()
        racket_2.reset()
        ball.reset()





        
        display.update()
    time.delay(50)

    
