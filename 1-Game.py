import pygame
pygame.init()

s_width= 700
s_height= 399
 
clock=pygame.time.Clock()

bulletsound=pygame.mixer.Sound(r'D:\Game\Sound\Gunshots.wav')
attacksound=pygame.mixer.Sound(r'D:\Game\Sound\attack.wav')

music=pygame.mixer.music.load(r'D:\Game\Sound\song.mp3')
pygame.mixer.music.play(-1)

win=pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Hit-man Game")
bg = pygame.image.load(r'D:\Game\Bg\bci.jpg')


def redraw():
    win.blit(bg,(0,0))
    obj.draw(win)
    obj1.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

    
class player(object):
    wlkright=[pygame.image.load(r'D:\Game\Hero\R1.png'),pygame.image.load(r'D:\Game\Hero\R2.png'),
              pygame.image.load(r'D:\Game\Hero\R3.png'),pygame.image.load(r'D:\Game\Hero\R4.png'),
              pygame.image.load(r'D:\Game\Hero\R5.png'),pygame.image.load(r'D:\Game\Hero\R6.png'),
              pygame.image.load(r'D:\Game\Hero\R7.png'),pygame.image.load(r'D:\Game\Hero\R8.png'),
              pygame.image.load(r'D:\Game\Hero\R9.png')]


    wlkleft=[pygame.image.load(r'D:\Game\Hero\L1.png'),pygame.image.load(r'D:\Game\Hero\L2.png'),
              pygame.image.load(r'D:\Game\Hero\L3.png'),pygame.image.load(r'D:\Game\Hero\L4.png'),
              pygame.image.load(r'D:\Game\Hero\L5.png'),pygame.image.load(r'D:\Game\Hero\L6.png'),
              pygame.image.load(r'D:\Game\Hero\L7.png'),pygame.image.load(r'D:\Game\Hero\L8.png'),
              pygame.image.load(r'D:\Game\Hero\L9.png')]
    

    def __init__(self):
        self.x=100
        self.y=300
        self.width=64
        self.height=64
        self.right=False
        self.left=False
        self.standing=True
        self.vel=3
        self.walk_count=0
        self.jump_count=11
        self.jump=False
        self.path=[0,s_width]
        self.hitbox=[self.x,self.y,self.width,self.height]
        self.visible=True
        self.health=40

            
    def draw(self,win):
       if self.visible:
            if self.walk_count>=27:
                self.walk_count=0
                
            if not (self.standing):
                if self.right:
                    win.blit(self.wlkright[self.walk_count//3],(self.x,self.y))
                    self.walk_count+=1
                    self.standing=True
                elif self.left:
                    win.blit(self.wlkleft[self.walk_count//3],(self.x,self.y))
                    self.walk_count+=1
                    self.standing=True
            else:
                if self.left:
                    win.blit(self.wlkleft[0],(self.x,self.y))
                else:
                    win.blit(self.wlkright[0],(self.x,self.y))

            self.hitbox=[self.x+20,self.y+5,25,60]
            pygame.draw.rect(win,(255,0,0),self.hitbox,-1)
            pygame.draw.rect(win,(255,255,255),(self.hitbox[0],self.hitbox[1]-15,40,8),1)
            if self.health<15:
                pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-15,self.health,8))
            else:
                pygame.draw.rect(win,(0,130,0),(self.hitbox[0],self.hitbox[1]-15,self.health,8))

    def hit(self):
        if self.health>0:
            self.health-=2
        else:
            self.visible=False
            end_scr()
        if self.right:
            self.x=self.x-50
        if self.left:
            self.x=self.x+50

class enemy(object):
    wlkright=[pygame.image.load(r'D:\Game\Enemy\R1.png'),pygame.image.load(r'D:\Game\Enemy\R2.png'),
              pygame.image.load(r'D:\Game\Enemy\R3.png'),pygame.image.load(r'D:\Game\Enemy\R4.png'),
              pygame.image.load(r'D:\Game\Enemy\R5.png'),pygame.image.load(r'D:\Game\Enemy\R6.png'),
              pygame.image.load(r'D:\Game\Enemy\R7.png'),pygame.image.load(r'D:\Game\Enemy\R8.png'),
              pygame.image.load(r'D:\Game\Enemy\R9.png'),pygame.image.load(r'D:\Game\Enemy\R10.png'),
              pygame.image.load(r'D:\Game\Enemy\R11.png')]


    wlkleft=[pygame.image.load(r'D:\Game\Enemy\L1.png'),pygame.image.load(r'D:\Game\Enemy\L2.png'),
              pygame.image.load(r'D:\Game\Enemy\L3.png'),pygame.image.load(r'D:\Game\Enemy\L4.png'),
              pygame.image.load(r'D:\Game\Enemy\L5.png'),pygame.image.load(r'D:\Game\Enemy\L6.png'),
              pygame.image.load(r'D:\Game\Enemy\L7.png'),pygame.image.load(r'D:\Game\Enemy\L8.png'),
              pygame.image.load(r'D:\Game\Enemy\L9.png'),pygame.image.load(r'D:\Game\Enemy\L10.png'),
              pygame.image.load(r'D:\Game\Enemy\L11.png')]
    
    
    def __init__(self):
        self.x=s_width
        self.y=310
        self.width=64
        self.height=64
        self.walk_count=0
        self.right=False
        self.left=False
        self.vel=2
        self.path=[0, s_width]
        self.hitbox=[self.x,self.y,self.width,self.height]
        self.health=40
        self.visible=True


    def draw(self,win):
        if self.visible:
            if self.walk_count>=33:
                self.walk_count=0
            if self.right:
                win.blit(self.wlkright[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
                
            elif self.left:
                win.blit(self.wlkleft[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
            pygame.draw.rect(win,(255,255,255),(self.hitbox[0],self.hitbox[1]-15,40,8),1)
            if self.health<15:
                pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-15,self.health,8))
            else:
                pygame.draw.rect(win,(0,130,0),(self.hitbox[0],self.hitbox[1]-15,self.health,8))

            
                
        
        
        self.hitbox=[self.x+18,self.y,40,57]
        pygame.draw.rect(win,(255,0,0),self.hitbox,-1)

        self.move()

      

    def move(self):
        if self.vel>0:
            if self.x+self.vel>self.path[0]: 
                self.x-=self.vel
                self.left=True
                self.right=False
            else:
                self.vel=self.vel*-1
        else:
            if self.x+self.vel+self.width<self.path[1]:
                self.x-=self.vel
                self.left=False
                self.right=True
            else:
                self.vel=self.vel*-1
     
    def hit(self):
        if self.health>0:
            self.health-=2
        else:
            self.visible=False
class fire:
    def __init__(self,x,y,facing):
        self.x=x
        self.y=y
        self.radius=5
        self.vel=15*facing
        
    def draw(self,win):
        pygame.draw.circle(win,(255,0,0),(self.x,self.y),self.radius)
        
    




def end_scr():
    global game_over
    if obj1.visible and not obj.visible:
        win.blit(bg,(0,0))
        img=pygame.image.load(r'D:\Game\Bg\lose.jpg')
        win.blit(img,(300,100))
        pygame.display.update()
        pygame.time.delay(2000)
        pic=pygame.image.load(r'D:\Game\Bg\govr.jpg')
        win.blit(pic,(220,100))
        pygame.display.update()
        pygame.time.delay(3000)
    else:
        win.blit(bg,(0,0))
        img=pygame.image.load(r'D:\Game\Bg\win.jpg')
        win.blit(img,(200,100))
        pygame.display.update()
        pygame.time.delay(2000)
        pic=pygame.image.load(r'D:\Game\Bg\govr.jpg')
        win.blit(pic,(220,90))
        pygame.display.update()
        pygame.time.delay(3000)
    game_over=True
   

    
       

    
lc=0
obj1=enemy()
obj=player()
bullets=[]
game_over= False
while not game_over:
    clock.tick(30)
    if lc>5:
        lc=0
    else:
        lc+=1

    if obj1.visible:
        if obj.hitbox[1] < obj1.hitbox[1] + obj1.hitbox[3] and obj.hitbox[1]+obj1.hitbox[3]>obj1.hitbox[1]:
            if obj.hitbox[0]+obj.hitbox[2]>obj1.hitbox[0] and obj.hitbox[0] < obj1.hitbox[0] + obj1.hitbox[2]:
                attacksound.play()
                obj.hit()
                
            
    else:
        end_scr()
        game_over=True
                
    
    for bullet in bullets:
        if bullet.y-bullet.radius < obj1.hitbox[1] + obj1.hitbox[3] and bullet.y+bullet.radius>obj1.hitbox[1]:
            if bullet.x + bullet.radius>obj1.hitbox[0] and bullet.x-bullet.radius <obj1.hitbox[0] + obj1.hitbox[2]:
                obj1.hit()
                bullets.pop(bullets.index(bullet))
           
                
        if bullet.x<s_width and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) 
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            game_over= True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and obj.x+obj.width+obj.vel<s_width:
            obj.right=True
            obj.left=False
            obj.standing=False
            obj.x+=obj.vel
        elif event.key == pygame.K_LEFT and obj.x>0:
            obj.right=False
            obj.left=True
            obj.standing=False
            obj.x-=obj.vel
        if not obj.jump:
            if event.key == pygame.K_UP:
                obj.jump=True
                obj.standing=True
                obj.walk_count=True
        if event.key == pygame.K_SPACE and lc==5:
            bulletsound.play()
            if obj.left:
                facing=-1
            else:
                facing=1
            if len(bullets)<5:
                bullets.append(fire(round(obj.x+obj.width//2),round(obj.y+obj.height//2),facing))
                
            

    if obj.jump:
        neg=1
        if obj.jump_count<0:
            neg=-1
        if obj.jump_count>=-11:
            obj.y-=(obj.jump_count ** 2)*0.5*neg
            obj.jump_count-=1
        else:
            obj.jump=False
            obj.jump_count=11


    redraw()

pygame.quit()
