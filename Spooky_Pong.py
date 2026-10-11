import pygame

pygame.init()
pygame.font.init()
W, H = 1200, 600
ball_radius = 15
WHITE = (255, 255, 255)

left_score = 0
right_score = 0
font = pygame.font.SysFont(None, 45)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Spooky_Pong')

class Game_Sprites(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (100, 100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_Sprites):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and self.rect.y < H - self.rect.height:
            self.rect.y += 5
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= 5
class Player2(Game_Sprites):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.rect.y < H - self.rect.height:
            self.rect.y += 5
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= 5

player1 = Player('images/spooky.png', 10, 40, 80)
player2 = Player2('images/spooky2.png', 1090, 40, 80)
ball = pygame.Rect(W//2 - ball_radius, H//2 - ball_radius, ball_radius*2, ball_radius*2)
ball_image = pygame.image.load('images/tikva.png')
ball_image = pygame.transform.scale(ball_image, (ball_radius*2, ball_radius*2))

ball_speedX = 7
ball_speedY = 7

def draw_ball():
    screen.blit(ball_image, (ball.x, ball.y))

def reset_ball():
    global ball_speedX, ball_speedY
    ball.center = (W//2, H//2)
    ball_speedX *= -1

time = pygame.time.Clock()
FPS = 60
run = True
final = False


while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if final != True:
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()

        draw_ball()
        ball.x += ball_speedX
        ball.y += ball_speedY

        if ball.top <= 0 or ball.bottom >= H:
            ball_speedY *= -1

        if ball.colliderect(player1) and ball_speedX < 0:
            ball_speedX *= -1
        if ball.colliderect(player2) and ball_speedX > 0:
            ball_speedX *= -1

        left_text = font.render(str(left_score), True, WHITE)
        screen.blit(left_text, (W//4 - left_text.get_width() // 2, 20))

        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(right_text, (3*W//4 - right_text.get_width() // 2, 20))

        if ball.left <= 0:
            right_score += 1
            reset_ball()
        if ball.right >= W:
            left_score += 1
            reset_ball()

        if left_score > 3:
            final = True
            win = font.render('LEFT SPOOKY WINNER!', True, (0, 255, 0))
            screen.blit(win, (255, 255))

        if right_score > 3:
            final = True
            win2 = font.render('RIGHT SPOOKY WINNER!', True, (0, 255, 0))
            screen.blit(win2, (255, 255))
            
        time.tick(FPS)
        pygame.display.flip()
pygame.quit()
