import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bee"] = pygame.image.load("bee.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["over"] = pygame.image.load("gameover.png").convert_alpha()
groundx=0

score=0
score_font=pygame.font.Font('freesansbold.ttf', 25)#

class Bee:
    speed=5
    g=0.5
    bee= pygame.Rect(100,250,30,30)

    def gravity(self):
        self.speed=self.speed+self.g
        self.bee.y= self.bee.y + self.speed

    def flap(self):
        self.speed=-10
    
    def display(self):
        screen.blit(images["bee"],self.bee) 

class Pipe:
    score=0 #Creating class variables for keeping the score
    count=0
    def __init__(self,x):
        Pipe.count=Pipe.count+1
        self.gap=random.randint(150, 400)
        self.topPipe=pygame.Rect(x,self.gap-400,40,320)
        self.bottomPipe=pygame.Rect(x,self.gap+100,40,320)
        
    def display(self):
        screen.blit(images["pipe"],self.topPipe)
        screen.blit(images["pipe"],self.bottomPipe)
        #pygame.draw.rect(screen,(250,150,50),pygame.Rect(200,self.gap,100,100))
    
    def move(self):
        self.topPipe.x-=5
        self.bottomPipe.x-=5   
        if self.topPipe.x<-40:
            self.topPipe.x=400
            self.bottomPipe.x=400
            self.gap=random.randint(150, 400)
            self.topPipe.y=self.gap-400
            self.bottomPipe.y=self.gap+100
        if self.topPipe.x==100: #Checking if pipe has crossed the bee
            Pipe.score=Pipe.score+1  #Incrementing the score 
          
bee=Bee()
pipe1= Pipe(300)
pipe2= Pipe(520)
state="play"

while True:    
    screen.fill((50,150,255))
    screen.blit(images["bg"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bee.flap()
    
    print(Pipe.count)
    bee.gravity() 
    
    if groundx< -330:
        groundx=0
        
    if bee.bee.colliderect(pipe1.topPipe) or bee.bee.colliderect(pipe1.bottomPipe) or bee.bee.colliderect(pipe2.topPipe) or bee.bee.colliderect(pipe2.bottomPipe) :
        state="over"
     
    if state=="play":
        bee.display()  
        pipe1.display() 
        pipe2.display() 
        groundx =groundx-5
        pipe1.move()
        pipe2.move()
        #Displaing the sore using Pipe.score
        score_text=score_font.render(str(Pipe.score), False, (255,255,0))  
        screen.blit(score_text,[200,10]) 
    
    if state=="over":
        screen.blit(images["over"],[100,200])
    
    screen.blit(images["base"],[groundx,550])
    pygame.display.update() 
    clock.tick(30) 
    
    
    
    

