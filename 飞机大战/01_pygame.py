import pygame
from plane_sprites import *

pygame.init()
# 绘制屏幕大小
screen = pygame.display.set_mode((480,700))
# 加载背景
background = pygame.image.load("./images/background.png")


# 加载飞机
hreo_rect = pygame.Rect(200,500,102,126)
hreo = pygame.image.load('./images/me1.png')
# 设置时钟
clock = pygame.time.Clock()

# 创建精灵
enemy = GameSprite("./images/enemy1.png")

#　创建经精灵组
enemy_group = pygame.sprite.Group(enemy)


# 循环游戏
while True:

    # 设置循环频率
    clock.tick(60)

    if hreo_rect.y + hreo_rect.height <= 0:
        hreo_rect.y = 700
    screen.blit(background, (0, 0))
    screen.blit(hreo,hreo_rect)
    # 配置精灵组
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
    hreo_rect.y -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.close()
            exit()


#
pygame.close()