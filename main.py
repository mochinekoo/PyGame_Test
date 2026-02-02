import pygame
import sys

# 初期化
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("テストゲームだよ")
screen.fill((0, 255, 0))

# ゲーム
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.flip()