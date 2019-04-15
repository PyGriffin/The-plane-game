import pygame
from plane_sprites import *

class PlaneGame(object):
    """

    """


    def __init__(self):

        # 创建窗口
        pygame.init()
        self.screed = pygame.display.set_mode(SCREED_RECT.size)

        # 创建时钟
        self.clock = pygame.time.Clock()

        # 创建精灵和精灵组
        self.__sprite_group()

        # 设置敌机定时实践
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(BULLET_EVENT, 500)

    def __sprite_group(self):
        # 背景图片
        back1 = Background()
        back2 = Background(True)
        self.back_group = pygame.sprite.Group(back1,back2)

        # 敌机组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def __game_over(self):
        pygame.quit()
        exit()

    def __check_collide(self):
        # 敌机子弹碰撞检测
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemy_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemy_list) > 0:
            self.hero.kill()
            self.__game_over()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if event.type == CREATE_ENEMY_EVENT:
                print("敌机出现")
                # 创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            if event.type == BULLET_EVENT:
                print("子弹")
                self.hero.fire()


        # 按键获取
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0



    def __update_sprites(self):
        # 背景精灵组
        self.back_group.update()
        self.back_group.draw(self.screed)
        # 敌机精灵族
        self.enemy_group.update()
        self.enemy_group.draw(self.screed)

        self.hero_group.update()
        self.hero_group.draw(self.screed)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screed)



    def start_game(self):

        while True:
            # 刷新帧率
            self.clock.tick(CLOCK)

            # 监听事件
            self.__event_handler()
            # 碰撞事件
            self.__check_collide()
            # 设置精灵组
            self.__update_sprites()
            #　刷新屏幕现实
            pygame.display.update()



if __name__ == '__main__':
    pg = PlaneGame()
    pg.start_game()