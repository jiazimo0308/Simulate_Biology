#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
import random
import pygame
from Environment import Food
#初始化显示环境（pygame窗口）
pygame.init()
width,height=800,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('生物进化')
clock=pygame.time.Clock()
#创建生物
#随机生成食物
foods=[Food(random.randint(0,width),random.randint(0,height)) for _ in range(4)]#200为生成食物个数
#循环演化
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    for food in foods:
        if not food.is_eaten:
            size = food.nutrition  # 食物大小
            pygame.draw.circle(screen, (0, 255, 0), (food.x, food.y), size)  #
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
