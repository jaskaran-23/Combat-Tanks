
def tank(x,y,turpos):
    x=int(x)
    y=int(y)
    possibleturrets=[(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-24,y-11),(x-23,y-14),(x-22,y-17),(x-21,y-20),(x-20,y-23),(x-19,y-24),(x-18,y-25),(x-17,y-26),(x-16,y-27)]
    pygame.draw.circle(gamedisplay,black,(x,y),int(tankheight/2))
    pygame.draw.rect(gamedisplay,black,(x-tankheight,y,tankwidth,tankheight))
    pygame.draw.line(gamedisplay,black,(x,y),possibleturrets[turpos],turretwidth)
    #wheels
    pygame.draw.circle(gamedisplay,black,(x-15,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+15,y+20),wheelwidth)
   # pygame.draw.circle(gamedisplay,black,(x+20,y+20),wheelwidth)
    return possibleturrets[turpos]


def enemy_tank(x,y,turpos):
    x=int(x)
    y=int(y)
    possibleturrets=[(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+24,y-11),(x+23,y-14),(x+22,y-17),(x+21,y-20),(x+20,y-23),(x+19,y-24),(x+18,y-25),(x+17,y-26),(x+16,y-27),(x+17,y-29)]
    pygame.draw.circle(gamedisplay,black,(x,y),int(tankheight/2))
    pygame.draw.rect(gamedisplay,black,(x-tankheight,y,tankwidth,tankheight))
    pygame.draw.line(gamedisplay,black,(x,y),possibleturrets[turpos],turretwidth)
    #wheels
    pygame.draw.circle(gamedisplay,black,(x-15,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x-5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+5,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+10,y+20),wheelwidth)
    pygame.draw.circle(gamedisplay,black,(x+15,y+20),wheelwidth)
   # pygame.draw.circle(gamedisplay,black,(x+20,y+20),wheelwidth)
    return possibleturrets[turpos]
 
