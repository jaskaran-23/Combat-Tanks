
def health_bars(player_health,enemy_health):
    if player_health>=75:
        player_health_color=green
    elif player_health>=50:
        player_health_color=yellow
    else:
        player_health_color=red
        
    if enemy_health>=75:
        enemy_health_color=green
    elif enemy_health>=50:
        enemy_health_color=yellow
    else:
        enemy_health_color=red

    pygame.draw.rect(gamedisplay,player_health_color,(680,25,player_health,25))
    pygame.draw.rect(gamedisplay,enemy_health_color,(20,25,enemy_health,25))
        
