# _*_ coding:utf-8 _*_

import pygame
from pygame.locals import *
import time
import random
'''
1.搭建界面，完成窗口喝背景图的显示
'''
#创建一个飞机类
class heroplane(object):
    def __init__(self,screen_temp):
        self.x = 200
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = [] #存储发射出的子弹的引用

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5    
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#创建一个子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+40
        self.y = y-20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=5
    def judge(self):
        if self.y<0:
            return True
        else:
            return False
#创建一个敌机类
class enemy_plane(object):
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.bullet_list = [] #存储发射出的子弹的引用
        self.direction = "right"
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
               self.bullet_list.remove(bullet)
    def move(self):

        if self.direction=="right":
            self.x+=5
        elif self.direction=="left":
            self.x-=5
        if self.x>430:
            self.direction="left"
        elif self.x<0:
            self.direction="right"

    def fire(self):
        random_num=random.randint(1,100)
        if random_num==8 or random_num==20:

            self.bullet_list.append(enemy_bullet(self.screen,self.x,self.y))


#创建一个敌机子弹类
class enemy_bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+25
        self.y = y+40
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet1.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y+=5
    def judge(self):
        if self.y>852:
            return True
        else:
            return False
#获取事件，比如按键等
def key_control(hero_temp,):

    for event in pygame.event.get():

        #判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否按下了按键
        elif event.type == KEYDOWN:
            #检测键盘是否a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测键盘是否d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测键盘是否空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

def main():
    #1.创建一个窗口
   
    screen = pygame.display.set_mode((480,852),0,10)

    #2.创建一个背景图
    background = pygame.image.load("./feiji/background.png")
    
    #3.创建一个飞机对象
    hero = heroplane(screen)
    #4.创建敌机对象 
    enemy = enemy_plane(screen)
    while True:

        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)

        time.sleep(0.01)
if __name__ == "__main__":
    main()
