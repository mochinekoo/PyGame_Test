import pygame
import sys

def initGame():
    # 初期化
    pygame.init()
    global screen
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("テストゲームだよ")
    screen.fill((0, 255, 0))
    runGame()

def runGame():
    # ゲーム
    while True:
        update()
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.display.flip()

def draw():
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (1000, 101)) # 線
    pygame.draw.rect(screen, (255, 0, 0), (100, 150, 500, 500)) # 四角形
    pygame.draw.circle(screen, (0, 0, 0), (100, 200), 10) # 円

    font = pygame.font.Font("F:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\Fonts\\ロゴたいぷゴシック.otf", 40)
    text = font.render("ああ", True, (0, 0, 0))
    screen.blit(text, (600, 300)) # テキスト

def update():
    pass

if __name__ == '__main__':
    initGame()