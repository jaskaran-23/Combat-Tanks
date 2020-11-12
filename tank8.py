
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


