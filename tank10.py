

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
