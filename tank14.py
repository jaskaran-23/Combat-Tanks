      
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