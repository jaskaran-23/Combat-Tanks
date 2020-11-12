
def explosion(x,y,size=50):
    explode=True
    while explode ==True:
        for event in pygame.event.get():
            if event.type()==pygame.QUIT:
                pygame.quit()
                quit()
        start=x,y
        colorc=[red,light_red,yellow,light_yellow]
        mag=1
        while mag<size:#to avoid hard codi ng
            explode_x=x+random.randrange(-1*mag,mag)
            explode_y=y+random.randrange(-1*mag,mag)
            pygame.draw.circle(gamedisplay,colorc[random.randrange(0,4)],(explode_x,explode_y),random.randrange(1,5))
            mag+=1
            pygame.display.update()
            clock.tick(100)
        explode=False

