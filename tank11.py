
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


