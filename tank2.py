
def text_objects(text,color,size):
    if size=="small":
        textsurface=smallfont.render(text,True,color)
    if size=="medium":
        textsurface=medfont.render(text,True,color)
    if size=="large":
        textsurface=largefont.render(text,True,color)
    return textsurface,textsurface.get_rect()
