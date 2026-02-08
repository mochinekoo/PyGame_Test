import pygame
import sys
from pygame import Vector2

keyFlag = False
location = Vector2(100, 50)
vector = Vector2(1, 0)

def initGame():
    global keyFlag
    global font
    # 初期化
    pygame.init()
    global screen
    screen = pygame.display.set_mode((1280, 720))
    font = pygame.font.Font("F:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\Fonts\\ロゴたいぷゴシック.otf", 40)
    pygame.display.set_caption("テストゲームだよ")
    screen.fill((0, 255, 0))
    runGame()

def runGame():
    clock = pygame.time.Clock()
    # ゲーム
    while True:
        clock.tick(60)
        screen.fill((0, 255, 0))
        update()
        draw()
        pygame.display.flip()

def draw():
    global font
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (1000, 101)) # 線
    pygame.draw.rect(screen, (255, 0, 0), (100, 150, 500, 500)) # 四角形
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=location, radius=10) # 円

    text = font.render("ああ", True, (0, 0, 0))
    screen.blit(text, (600, 300)) # テキスト

    if keyFlag:
        screen.blit(font.render("押されてます", True, (0,0,0)), (50, 50))

def update():
    global keyFlag

    keys = pygame.key.get_pressed()

    if keys[pygame.K_0]:
        keyFlag = True
    if keys[pygame.K_d]:
        location.x += vector.x
    if keys[pygame.K_a]:
        location.x -= vector.x
    if keys[pygame.K_w]:
        location.y -= vector.x
    if keys[pygame.K_s]:
        location.y += vector.x

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                keyFlag = False

if __name__ == '__main__':
    initGame()