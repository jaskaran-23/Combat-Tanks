
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

