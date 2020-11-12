

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

