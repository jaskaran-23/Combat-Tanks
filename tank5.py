
def message_to_screen(msg,color,ydisp=0,size="small"):
   # screen_text=font.render(msg,True,color)
    #gamedisplay.blit(screen_text,[display_width/2,display_height/2])
   textsurface,textrect=text_objects(msg,color,size)
   textrect.center=(display_width/2),(display_height/2)+ydisp
   gamedisplay.blit(textsurface,textrect)
