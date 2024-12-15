# -*- coding: utf-8 -*-            
# @Author : Jiazimo

import random
#食物
class Food:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.nutrition=int(random.randint(20,30))
        self.is_eaten=False

