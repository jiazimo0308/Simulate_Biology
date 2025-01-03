# Simulate_Biology
模拟一个生物群落的进化，其中可以构建多个种群的生物进行资源竞争和生物繁衍新生代。  
Simulate the evolution of a biological community, where multiple populations of organisms can be constructed to compete for resources and reproduce into new generations.

## 项目的实现思路（Realization ideas of the project）
### 1.基本构建对象思路（Basic ideas for constructing objects）
#### 1.环境构建（Environmental construction）
为了模拟自然界真实生命体存活的环境，避免在项目起始阶段由于过多因素的影响而导致冗余问题的发生，由最简单的环境构成进行搭建。例如：通过大小展现出食物量或食物对生命体的效益。通过食物出现的随机位置展现出自然界中的随机性。后续可以根据具体主观意向进行环境设置。  
（In order to simulate the living environment of real life in nature and avoid the occurrence of redundancy problems due to the influence of too many factors at the beginning of the project, it is built from the simplest environment.For example:The size shows the amount of food or the benefits of food to living things. It shows the randomness in nature through the random position of food. In the future, the environment can be set according to specific subjective intentions.）

### 2.生命体构建（The construction of life forms）
构建简单的生命体属性特征。在生物学中，健康状况通常与年龄和食物的关系非常密切。例如：  
(Construct simple attributes of life forms. In biology, health is usually closely related to age and food.For example)  
1. 年龄：随着年龄的增长，生物的健康状况可能会逐渐下降。这是因为随着年龄的增长，生物的身体机能可能会逐渐衰退，导致健康状况下降。(Age: With age, the health of living things may gradually decline. This is because with age, the physical function of living things may gradually decline, resulting in a decline in health.)
2. 食物：食物是生物获取能量和营养的主要来源，对生物的健康状况有直接影响。如果生物能够获取充足和营养均衡的食物，那么它的健康状况可能会比较好。反之，如果生物的食物供应不足或营养不均衡，那么它的健康状况可能会下降。(Food: Food is the main source of energy and nutrition for organisms, which has a direct impact on the health of organisms. If an organism has access to adequate and balanced food, its health may be better. On the contrary, if the biological food supply is insufficient or nutritionally unbalanced, its health may decline.）

根据此构建模拟关系：(Build a simulation relationship according to this)  
1. 年龄：可以设置一个规则，使得生物的健康值每年都会下降一定的值。例如，可以设置每年健康值下降1。(Age: A rule can be set so that the health value of the organism decreases to a certain value every year. For example, you can set the annual decline in health value by 1. )
2. 食物：可以设置一个规则，使得生物每次吃食物时，其健康值都会增加一定的值。例如，可以设置每次吃食物，健康值增加10。(Food: A rule can be set so that every time a creature eats food, its health value will increase to a certain value. For example, you can set that every time you eat food, your health value will increase by 10.)

这只是一个基本的模拟，可以根据具体的需求来调整这些规则，赋予生命实体中不同的属性。   
(This is just a basic simulation, which can adjust these rules according to specific needs and give different attributes in living entities.）

### 2.整体发展思路（The overall development idea）
根据不断的调整相关参数进一步优化项目效果。并在单个种群的基础上进行种群扩展，或生命个体的属性自然变化。  
（Further optimize the effect of the project according to the continuous adjustment of relevant parameters. And carry out population expansion on the basis of a single population, or the natural change of the attributes of living individuals.）

## 模拟附加环境（Simulate the additional environment）
### 1.软件环境（Software environment）
实现模拟模型生物群落基于python语言，当前使用的python版本为3.10.9。当前使用到pygame，random,time,numpy库函数，后续如有用到新的库会进行说明。  
（The implementation of the simulation model biome is based on python language, and the python version currently used is 3.10.9. At present, the library functions of pygame, random, time and numpy are used. If a new library is used in the future, it will be explained.）
### 2.参数环境（Parameter environment）
设置项目窗口大小为长800，宽600的尺寸。（Set the size of the project window to 800 long and 600 wide.）  
设计整体的运行架构（Design the overall operating architecture）

    //设计整体的运行架构
    # -*- coding: utf-8 -*-            
    # @Author : Jiazimo
    import random
    import pygame
    
    #初始化显示环境（pygame窗口）
    pygame.init()
    width,height=800,600
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('生物进化')
    clock=pygame.time.Clock()
    
    #创建生命体
    #生成食物
    
    #循环
    running=True
    while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    
    #加入生物动作
    
    pygame.display.flip()
    clock.tick(60)
    pygame.quit()

# 第一阶段的实现（The realization of the first stage）
## 1.环境构建（Environmental construction）
环境的构建通过最简单的方式进行，设置食物的大小，位置，以及是否被吃掉。食物属性如下表所示。  
(The construction of the environment is carried out in the simplest way, setting the size, position, and whether the food is eaten. Food attributes are shown in the table below.)  

<div align=center>

**食物属性表**
|食物|属性|
|:----:|:----:|
|横坐标位置|x|
|纵坐标位置|y|
|食物大小|nutrition|
|是否被吃掉|True/False|
</div>

环境构建（Environmental construction）

    //环境构建
    # -*- coding: utf-8 -*-            
    # @Author : Jiazimo
    import random
    
    #食物
    class Food:
    def __init__(self,x,y):
        self.x=x#食物的横坐标
        self.y=y#食物的纵坐标
        self.nutrition=int(random.randint(20,30))#食物大小
        self.is_eaten=False#食物是否被吃掉
通过环境构建展现到整体运行架构。(The overall operation architecture is displayed through environmental construction.)

    # -*- coding: utf-8 -*-            
    # @Author : Jiazimo
    import random
    import pygame
    from Environment import Food
    
    pygame.init()
    width,height=800,600
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('生物进化')
    clock=pygame.time.Clock()
    foods=[Food(random.randint(0,width),random.randint(0,height)) for _ in range(4)]#生成四个食物
    #循环
    running=True
    while running:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
      screen.fill((255,255,255))
      
      for food in foods:
       if not food.is_eaten:
          size=food.nutrition#食物大小
          pygame.draw.circle(screen, (0, 255, 0), (food.x, food.y), size)#展现食物

          pygame.display.flip()
      clock.tick(60)
    pygame.quit()
在当前窗口内展现食物。 (Display the food in the current window) 
<div align=center>
<img width="400" alt="截屏2024-12-15 14 15 01" src="https://github.com/user-attachments/assets/9b0142af-6637-4b8f-9d0d-2a012799c5ce" />
</div>

## 2.生物个体构建（Biological individual construction）

生物体我们以种群为单位进行构建。创建List集合存放生成的种群个体，根据给定的参数生成种群中个体的数量，并根据生成的随机位置创建种群中的个体，并将创建成功的个体保存在种群List中。  

种群的产生

    def making(a,width,height):
    '''a,初始个数'''
    creaturesA = []
    num_creaturesA = a
    for _ in range(num_creaturesA):
        x = random.randint(0, width)
        y = random.randint(0, height)
        creaturesa = living.Creature(x, y)//产生单个物种
        creaturesA.append(creaturesa)
    return creaturesA

而后是对单个种群物种的属性定义。最基本的有种群中个体的位置，种群中个体的年龄，种群中个体的生成速度，种群中个体的天赋能力(这里的天赋能力以种群中个体移动的速度作为种群个体的天赋，移动速度越快，种群个体获得食物的概率越大)，种群个体身体健康状况，以及种群个体的性别，和种群个体代数以及每一代对应于不同的颜色。

<div align=center>

**种群个体属性表**
|种群个体|属性|
|:----:|:----:|
|横坐标位置|x|
|纵坐标位置|y|
|年龄|year|
|个体生长速度|speed_grow|
|天赋能力|speed_base|
|健康状况|health|
|性别|gender|
|是否存活|is_alive|
|代数|generation|
|代数对应的颜色更新|update_color()|
</div>


## 后续更新中。。。。（In the follow-up update...）


