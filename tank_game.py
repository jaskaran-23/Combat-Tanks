import pygame
import time
import random
pygame.init()
white1=(255,255,255)
black=(0,0,0)
red=(200,0,0)
light_red=(255,0,0)
green=(0,225,0)
yellow=(240,240,0)
light_yellow=(255,255,0)
light_green=(0,255,0)
light_blue=(173,216,230)
display_width=800
display_height=600

gamedisplay=pygame.display.set_mode((display_width,display_height))

pygame.mixer.music.load("goat.mp3")
pygame.mixer.music.play(-1)



pygame.display.set_caption("TANKS")

icon=pygame.image.load("apple.png")
pygame.display.set_icon(icon)

pygame.display.update()
#img=pygame.image.load("snakehead.png")
#appleimg=pygame.image.load("apple.png")

#block_size=20
#apple_size=50
clock=pygame.time.Clock()
FPS=20
direction="right"
smallfont=pygame.font.SysFont("comicsansms",25)          
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("arial",75)

 
tankwidth=40
tankheight=20

turretwidth=5
wheelwidth=5

ground_height=35

def text_objects(text,color,size):
    if size=="small":
        textsurface=smallfont.render(text,True,color)
    if size=="medium":
        textsurface=medfont.render(text,True,color)
    if size=="large":
        textsurface=largefont.render(text,True,color)
    return textsurface,textsurface.get_rect()


def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
    textsurface,textrect=text_objects(msg,color,size)
    textrect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    gamedisplay.blit(textsurface,textrect)



def button(text,x,y,width,height,inactive_color,active_color, action=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+width>cur[0] and cur[0]>x and y+height>cur[1] and cur[1]>y:
        pygame.draw.rect(gamedisplay,active_color,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="quit":
                pygame.quit()
                quit()
            elif action=="controls":
                game_controls()
            elif action=="play":
                gameLoop()
            elif action=="main":
                intro()
            
    else:
        pygame.draw.rect(gamedisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)


def message_to_screen(msg,color,ydisp=0,size="small"):
   # screen_text=font.render(msg,True,color)
    #gamedisplay.blit(screen_text,[display_width/2,display_height/2])
   textsurface,textrect=text_objects(msg,color,size)
   textrect.center=(display_width/2),(display_height/2)+ydisp
   gamedisplay.blit(textsurface,textrect)

def tank(x,y,turpos):
    x=int(x)
    y=int(y)
    possibleturrets=[(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-24,y-11),(x-23,y-14),(x-22,y-17),(x-21,y-20),(x-20,y-23),(x-19,y-24),(x-18,y-25),(x-17,y-26),(x-16,y-27)]
    pygame.draw.circle(gamedisplay,black,(x,y),int(tankheight/2))
    pygame.draw.rect(gamedisplay,black,(x-tankheight,y,tankwidth,tankheight))
    pygame.draw.line(gamedisplay,black,(x,y),possibleturrets[turpos],turretwidth)
    #wheels
    pygame.draw.circle(gamedisplay,black,(x-15,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+15,y+20),wheelwidth)
   # pygame.draw.circle(gamedisplay,black,(x+20,y+20),wheelwidth)
    return possibleturrets[turpos]


def enemy_tank(x,y,turpos):
    x=int(x)
    y=int(y)
    possibleturrets=[(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+24,y-11),(x+23,y-14),(x+22,y-17),(x+21,y-20),(x+20,y-23),(x+19,y-24),(x+18,y-25),(x+17,y-26),(x+16,y-27),(x+17,y-29)]
    pygame.draw.circle(gamedisplay,black,(x,y),int(tankheight/2))
    pygame.draw.rect(gamedisplay,black,(x-tankheight,y,tankwidth,tankheight))
    pygame.draw.line(gamedisplay,black,(x,y),possibleturrets[turpos],turretwidth)
    #wheels
    pygame.draw.circle(gamedisplay,black,(x-15,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+15,y+20),wheelwidth)
   # pygame.draw.circle(gamedisplay,black,(x+20,y+20),wheelwidth)
    return possibleturrets[turpos]
 

def explosion(x,y,size=50):
    explode=True
    while explode ==True:
        for event in pygame.event.get():
            if event.type()==pygame.QUIT:
                pygame.quit()
                quit()
        start=x,y
        colorc=[red,light_red,yellow,light_yellow]
        mag=1
        while mag<size:#to avoid hard codi ng
            explode_x=x+random.randrange(-1*mag,mag)
            explode_y=y+random.randrange(-1*mag,mag)
            pygame.draw.circle(gamedisplay,colorc[random.randrange(0,4)],(explode_x,explode_y),random.randrange(1,5))
            mag+=1
            pygame.display.update()
            clock.tick(100)
        explode=False


def fire(xy,maintankx,maintanky,turpos,firepower,xlocation,barrier_width,randomheight,enemytankx,enemytanky):
    damage=0
    fire=True
    start=list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        print(start[0],start[1])
        pygame.draw.circle(gamedisplay,green,(start[0],start[1]),5)
        start[0]-=(15-turpos)*2
        start[1]+=int(((start[0]-xy[0])*0.015/(firepower/50))**2-(turpos+(turpos/(12-turpos))))
        if start[1]>display_height-ground_height:
            hitx=int((start[0]*(display_height-ground_height))/start[1])
            hity=int(display_height-ground_height)
            if enemytankx+15>hitx>enemytankx-15:
                damage=20
            explosion(hitx,hity)
            fire=False 
        check1=start[0]<=xlocation+barrier_width
        check2=start[0]>=xlocation
        check3=start[1]<=display_height
        check4=start[1]>=display_height-randomheight
        if check1 and check2 and check3 and check4:
            
            hitx=int((start[0]))
            hity=int(start[1])
            if enemytankx+10>hitx>enemytankx-10:
                damage=25
            elif enemytankx+15>hitx>enemytankx-15:
                damage=18
            elif enemytankx+25>hitx>enemytankx-25:
                damage=10
            elif enemytankx+30>hitx>enemytankx-30:
                damage=5
            explosion(hitx,hity)
            fire=False 
            
        pygame.display.update()
        clock.tick(50)
    return damage


def enemy_fire(xy,maintankx,maintanky,turpos,firepower,xlocation,barrier_width,randomheight,ptankx,ptanky):
    damage=0
    
    currentpower=1
    power_found=False
    while not power_found:
        currentpower+=1
        if currentpower>100:
            power_found=True  
        fire=True
        start=list(xy)
        while fire:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            #print(start[0],start[1])
            #pygame.draw.circle(gamedisplay,green,(start[0],start[1]),5)
            start[0]+=(15-turpos)*2
            start[1]+=int(((start[0]-xy[0])*0.015/(currentpower/50))**2-(turpos+(turpos/(12-turpos))))
            if start[1]>display_height-ground_height:
                hitx=int((start[0]*(display_height-ground_height))/start[1])
                hity=int(display_height-ground_height)
                #explosion(hitx,hity)
                if ptankx+15>hitx>ptankx-15:
                    power_found=True
                fire=False
                
            check1=start[0]<=xlocation+barrier_width
            check2=start[0]>=xlocation
            check3=start[1]<=display_height
            check4=start[1]>=display_height-randomheight
            if check1 and check2 and check3 and check4:
                
                hitx=int((start[0]))
                hity=int(start[1])
                #explosion(hitx,hity)
                fire=False


        
        
    fire=True
    start=list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        print(start[0],start[1])
        pygame.draw.circle(gamedisplay,green,(start[0],start[1]),5)
        start[0]+=(15-turpos)*2

        gun_power=random.randrange(int(currentpower*0.90),int(currentpower*1.10))
        
        start[1]+=int(((start[0]-xy[0])*0.015/(gun_power/50))**2-(turpos+(turpos/(12-turpos))))
        if start[1]>display_height-ground_height:
            hitx=int((start[0]*(display_height-ground_height))/start[1])
            hity=int(display_height-ground_height)
            if ptankx+10>hitx>ptankx-10:
                damage=25
            elif ptankx+15>hitx>ptankx-15:
                damage=18
            elif ptankx+25>hitx>ptankx-25:
                damage=10
            elif ptankx+30>hitx>ptankx-30:
                damage=5
            explosion(hitx,hity)
            fire=False  
        check1=start[0]<=xlocation+barrier_width
        check2=start[0]>=xlocation
        check3=start[1]<=display_height
        check4=start[1]>=display_height-randomheight
        if check1 and check2 and check3 and check4:
            
            hitx=int((start[0]))
            hity=int(start[1])
            explosion(hitx,hity)
            fire=False 
            
        pygame.display.update()
        clock.tick(50)
    return damage



def game_controls():
    
    gcont=True
    while gcont ==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
        gamedisplay.fill(light_blue)
        message_to_screen("Controls..",green,-100,"large")
        message_to_screen("fire :Space bar",red,-10,"medium")
        message_to_screen("Move using up and down arrows..",black,40,"small")
        message_to_screen("Pause :P!!!",red,100,"medium")
        # message_to_screen("Press C to play else Q to quit...",black,180,"medium")


        button("play",150,500,100,50,green,light_green,"play")
        button("main",350,500,100,50,yellow,light_yellow,"main")
        button("quit",550,500,100,50,red,light_red,"quit")
        

        
        pygame.display.update()
        clock.tick(15)




def pause():
    paused=True
    
    message_to_screen("Paused",red,-100,size="large")
    message_to_screen("Press C to continue or Q to quit.",black,25,"medium")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        #gamedisplay.fill(light_blue)
        message_to_screen("Paused",red,-100,size="large")
        message_to_screen("Press C to continue or Q to quit.",black,25,"medium")
        pygame.display.update()
        clock.tick(5)

def barrier(xlocation,random_height,barrier_width):
    pygame.draw.rect(gamedisplay,black,[xlocation,display_height-random_height,barrier_width,random_height])



def score(score):
    text=smallfont.render("Score: "+str(score),True,black)
    gamedisplay.blit(text,[0,0])


def power(level):
    text=medfont.render('Power is ' +str(level)+'%' ,True,black)
    gamedisplay.blit(text,[display_width/2-100,0])
    

def intro():
    intro=True
    while intro ==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                
        gamedisplay.fill(light_blue)
       # tank(maintankx,maintanky)

        
        message_to_screen("Welcome to TANKS..",green,-100,"large")
        message_to_screen("Objective is to shoot out enemy :D",red,-10,"medium")
        message_to_screen("Gain maximum points...",black,40,"small")
        message_to_screen("All the best!!!",red,100,"medium")
        # message_to_screen("Press C to play else Q to quit...",black,180,"medium")


        button("play",150,500,100,50,green,light_green,"play")
        button("control",350,500,100,50,yellow,light_yellow,"controls")
        button("quit",550,500,100,50,red,light_red,"quit")
        

        
        pygame.display.update()
        clock.tick(15)


def game_over():
    game_over=True
    while game_over ==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
        gamedisplay.fill(light_blue)
       # tank(maintankx,maintanky)

        
        message_to_screen("Game Over..",green,-100,"large")
        message_to_screen("You Die :(",red,-10,"medium")


        button("play Again",150,500,100,50,green,light_green,"play")
        button("control",350,500,100,50,yellow,light_yellow,"controls")
        button("quit",550,500,100,50,red,light_red,"quit")
        

        
        pygame.display.update()
        clock.tick(15)


def you_win():
    win=True
    while win ==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
        gamedisplay.fill(light_blue)
       # tank(maintankx,maintanky)

        
        message_to_screen("You win :)",green,-100,"large")
        message_to_screen("Congratulations :D",red,-10,"medium")


        button("play Again",150,500,100,50,green,light_green,"play")
        button("control",350,500,100,50,yellow,light_yellow,"controls")
        button("quit",550,500,100,50,red,light_red,"quit")
        

        
        pygame.display.update()
        clock.tick(15)

def health_bars(player_health,enemy_health):
    if player_health>=75:
        player_health_color=green
    elif player_health>=50:
        player_health_color=yellow
    else:
        player_health_color=red
        
    if enemy_health>=75:
        enemy_health_color=green
    elif enemy_health>=50:
        enemy_health_color=yellow
    else:
        enemy_health_color=red

    pygame.draw.rect(gamedisplay,player_health_color,(680,25,player_health,25))
    pygame.draw.rect(gamedisplay,enemy_health_color,(20,25,enemy_health,25))
        
def gameLoop():
    gameexit=False
    gameover=False
    player_health=100
    enemy_health=100
    
    
    maintankx=display_width*0.9
    maintanky=display_height*0.9
    tankmove=0


    currturrpos=0
    changetur=0
    barrier_width=50

    firepower=50
    powerchange=0

    enemytankx=display_width*0.1
    enemytanky=display_height*0.9
    
    xlocation=(display_width/2)+random.randint(-0.1*display_width,0.1*display_width)
    random_height=random.randrange(0.1*display_height,0.6*display_height)
    
    while not gameexit:
        
        while gameover==True:
            gamedisplay.fill(light_blue)
            message_to_screen("Game over",red,-50,size="large")
            message_to_screen("Press c to play again else q to quit",black,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameover=False
                    gameexit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameexit=True
                        gameover=False
                    elif event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
               gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    tankmove=-5
                elif event.key==pygame.K_RIGHT:
                    tankmove=5
                elif event.key==pygame.K_DOWN:
                    changetur=-1
                elif event.key==pygame.K_UP:
                    changetur=1
                elif event.key==pygame.K_p:
                    pause()
                elif event.key==pygame.K_SPACE:
                    damage1=fire(gun,maintankx,maintanky,currturrpos,firepower,xlocation,barrier_width,random_height,enemytankx,enemytanky)
                    enemy_health-=damage1
                    possiblemovement=['f','r']
                    moveindex=random.randrange(0,2)
                    for x in range(random.randrange(0,10)):
                        if display_width*0.3>enemytankx>display_width*0.03:
                            if possiblemovement[moveindex]=='f':
                                enemytankx+=5
                            elif possiblemovement[moveindex]=='r':
                                enemytankx-=5
                            gamedisplay.fill(light_blue)
                            health_bars(player_health,enemy_health)
                            gun=tank(maintankx,maintanky,currturrpos)
                            enemygun=enemy_tank(enemytankx,enemytanky,9)
                                                
                            power(firepower)
                                
                            
                           # print(gun)
                            barrier(xlocation,random_height,barrier_width)

                            gamedisplay.fill(green,rect=[0,display_height-ground_height,display_width,ground_height])
                            pygame.display.update()
                            clock.tick(FPS)
                            
                                                                
                    
                    damage=enemy_fire(enemygun,enemytankx,enemytanky,10,60,xlocation,barrier_width,random_height,maintankx,maintanky)
                    player_health-=damage
                elif event.key==pygame.K_a:
                    powerchange=1
                elif event.key==pygame.K_d:
                    powerchange=-1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tankmove=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    changetur=0
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    powerchange=0
                    
        maintankx+=tankmove
        currturrpos+=changetur
        if currturrpos<0:
            currturrpos=0
        elif currturrpos>11:
            currturrpos=11

        if maintankx-(tankwidth/2)<xlocation+barrier_width:
            maintankx+=5
        if maintankx+(tankwidth/2)>display_width:
            maintankx-=5

        
        gamedisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun=tank(maintankx,maintanky,currturrpos)
        enemygun=enemy_tank(enemytankx,enemytanky,9)
        firepower+=powerchange
        if firepower>100:
            firepower=100
        if firepower<5:
            firepower=5

        power(firepower)
            
        
       # print(gun)
        barrier(xlocation,random_height,barrier_width)

        gamedisplay.fill(green,rect=[0,display_height-ground_height,display_width,ground_height])
        clock.tick(FPS)
       # message_to_screen("Congrats",red)
        pygame.display.update()
        if player_health<1:
            game_over()
        elif enemy_health<1:
            you_win()
   # time.sleep(2)
    pygame.quit()
    quit()
intro()
gameLoop()
