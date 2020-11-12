
def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
    textsurface,textrect=text_objects(msg,color,size)
    textrect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    gamedisplay.blit(textsurface,textrect)


