
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

