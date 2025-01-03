# Simulating Biology
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
<img width="450" alt="截屏2025-01-03 13 20 12" src="https://github.com/user-attachments/assets/404d43ed-9e58-4c5b-b735-98a67360efbb" />
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

当个体吃到食物时此时个体的健康值加一

     def food1(self,food):
        self.health=self.health+food #根据食物更新健康状态

伴随着年龄每秒（年）钟生长1岁，自然条件下健康值每秒（年）自然下降1，行动速度为物种捕猎能力，能力由天赋与后天形成，整体受到年龄，健康状态，食物有关，当100岁或健康值为0时此生物死亡。因此随着年龄的变化所导致的其他属性的变化就由定义的years()函数进行确定。

      def years(self):
      
        '''年龄每秒（年）钟生长1岁，自然条件下健康值每秒（年）自然下降1，
        行动速度为物种捕猎能力，能力由天赋与后天形成，整体受到年龄，健康状态，
        食物有关，当100岁或健康值为0时此生物死亡'''
        
        self.year += 1 #假设自然状态下，每秒（年）年龄增加1
        self.health-=1  #假设自然状态下，健康值随每年下降1
        
        # 行动速度(与年龄，健康状态，食物有关)

        在这里normal_distribution是定义了一个正太函数，其中正太函数为
        def normal_distribution(x, mu, sigma):
            return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
            
        updata_speed=normal_distribution(self.year, 50, 10)*100 #假设50岁时能力达到最大
        self.speed=self.speed_base*updata_speed*self.health
        self.speed=int(max(0,min(50,self.speed))) #更新物种个体的速度值    
        
        #根据物种个体的速度值更新物种个体下一个前进的随机方向
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)

        #当健康值为0或年龄到达100岁时改变物种个体存在的状态
        if self.year==100 or self.health==0:
            self.is_alive=False
通过环境构建展现到整体运行架构。(The overall operation architecture is displayed through environmental construction.)  
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-            
    # @Author : Jiazimo
    import random
    import pygame
    from Environment import Food
    import BiotaInitialization
    #初始化显示环境（pygame窗口）
    pygame.init()
    width,height=800,600
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('生物进化')
    clock=pygame.time.Clock()
    #创建生物
    creatures = BiotaInitialization.making(20, width, height)#2为初始生物个数
    #循环演化
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill((255,255,255))
        for creature in creatures[:]:
            if creature.is_alive:#判断生物是否已经死亡
                creature.years()
                #雌性与雄性进行分类
                if creature.gender =='male':#雄性与雌性用不同的标准表示
                    pygame.draw.rect(screen,creature.color,pygame.Rect(creature.x,creature.y,10,10))#雄性使用方形表示
                else:
                    pygame.draw.circle(screen, creature.color, (creature.x, creature.y), 5)#雌性使用三角表示
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    
在当前窗口内展现种群。  
<div align=center>
    
![j_i-2025-01-01-12 55 42](https://github.com/user-attachments/assets/635b9337-3335-49ae-bce6-a3052c39078e)
</div>

## 3.生物个体与当前环境的联系
根据上述的两个构建，现构建种群个体获取环境食物的的关系。如果当前种群个体在食物大小设定的范围之内则判定食物被种群个体所吃掉。种群个体吃掉食物使得种群个体相对应的属性参数进行更新同样对当前吃掉的食物进行属性更新，刷新食物列表，删除已经被吃掉的食物并再生成一个新的食物。如果食物一旦被吃掉就不再检查其他生物的位置。

            for creature in creatures[:]:#查看生物是否在食物位置
                if abs(creature.x-food.x)<=size and abs(creature.y-food.y)<=size: #更改食物状态，更改生物状态
                    food.is_eaten=True #更改食物状态
                    creature.food1(food.nutrition) #对物种个体健康值进行更新
                    
                    #更新食物
                    new_food= Food(random.randint(0, width), random.randint(0, height)) #如果食物被吃掉一个则在随机位置生成一个随机大小的食物
                    foods.append(new_food) #添加新的食物
                    foods = [food for food in foods if not food.is_eaten] #刷新食物列表，删除已经被吃掉的食物自动删除
                    break #退出内部循环，一旦食物被吃掉就可以不用检查其他生物的位置了

在当前窗口展现种群与食物的效果
<div align=center>

![j_i-2025-01-01-18 12 48](https://github.com/user-attachments/assets/d4bd6f63-bdfe-407a-beaa-d086430343eb)
</div>

## 4.生物个体的交配、突变与变异
首先要产生后代，后代需要雌性与雄性交配所得到，在种群繁衍过程中要保证种群中不同的性别进行交配，雌性与雄性的健康要大于80，年龄在20到35之间，交配过后产生0到3个新个体且产生的后代性别随机，并在交配过程中加入遗传与变异的设定。其中雌性与雄性交配的条件为：  
&emsp;&emsp;1.保证当前雌性与雄性在相同的位置  
&emsp;&emsp;2.保证双方为不同的性别  
&emsp;&emsp;3.保证雌性与雄性的健康值大于80   
&emsp;&emsp;4.保证双方的年龄在20到35岁之间  
最终产生0到3个新个体。

    if self.x==other.x and self.y==other.y:#两者位置在相同位置才能进行交配
        #个体交配条件
        ‘’‘if (self.gender == 'male' and 10<=self.year <=35  and other.gender == 'female' and 10<=other.year<=30 and self.health>=20 and other.health>=20) or \
            (self.gender == 'male' and 10<=self.year <=35 and other.gender == 'female' and 10<=other.year<=30 and self.health>=20 and other.health>=20):'''
        
        #产生新的个体
        if self.gender!=other.gender:
            child = BiotaInitialization.making(random.choice([0,1,2,3]),width,height)#设定随机产生后代的个数
            print('产生'+str(len(child))+'后代')

遗传变异的设定是根据其新一代的父辈个体进行设定，并在不同个体交配过程中发挥作用。根据双方父母的参数，主要在起始的健康值与天赋能力上进行变化。首先定义一个变异的概率从0%到100%的概率，假设有X的概率发生变异，若变异率大于不发生变异的概率则随机选择改变speed_base或health。

    def variation(self):
    '''变异，假设只根据双方父母的参数，主要是起始健康与天赋能力'''
    mutation_chance = random.randint(0, 100) #变异率0%到100%
    mutation_chance_l=40 #假设有X的概率发生变异
    if mutation_chance >(100-mutation_chance_l):
        if random.choice([True, False]):  #随机选择改变speed_base或health
            self.speed_base = random.randint(0, 10)
        else:
            self.health = random.randint(0, 100)

将两种情况加入到雌性与雄性的交配函数中，

       def sex(self,other,width,height):
        '''不同性别的进行交配，健康要大于80，年年龄20-35，产生0-3个新个体性别随机，加入遗传与变异产生后代'''
        if self.x==other.x and self.y==other.y:#两者位置在相同位置才能进行交配
            '''
            if (self.gender == 'male' and 10<=self.year <=35  and other.gender == 'female' and 10<=other.year<=30 and self.health>=20 and other.health>=20) or \
                (self.gender == 'male' and 10<=self.year <=35 and other.gender == 'female' and 10<=other.year<=30 and self.health>=20 and other.health>=20):'''
            if self.gender!=other.gender:
                child = BiotaInitialization.making(random.choice([0,1,2,3]),width,height)#设定随机产生后代的个数
                print('产生'+str(len(child))+'后代')
                #根据父母双方进行合理的突变与变异
                children = []
                for c in child:
                    c.generation=max(self.generation,other.generation)+1#更新代数
                    c.update_color()#更新颜色
                    print('第'+str(c.generation)+'代')
                    #遗传
                    c.speed_base =(self.speed_base + other.speed_base) / 2 + random.randint(-2,2)# 基于父母的speed_base，再加上一些随机变化,
                    c.health = (self.health + other.health) / 2 + random.randint(-10, 10)  # 基于父母的health，再加上一些随机变化
                    #变异
                    c.variation()  # 对新生物进行可能的变异
                    c.speed_base = min(10, max(-10, c.speed_base))#确保数值在正常范围内-10～10
                    c.health= min(100, max(0, c.health))#确保数值在正常范围内0-100
                    children.append(c)
                print('实际后代数'+str(len(children)))
                return children
在当前窗口展现整体效果  

<div align=center>
    
https://github.com/user-attachments/assets/ea20b2d8-eae9-4aa2-8804-84194ab5f4b1

</div>


## 后续更新中。。。。（In the follow-up update...）



























