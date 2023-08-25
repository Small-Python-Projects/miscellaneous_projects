import random

I_points = 0
O_points = 0

I_games = 0
O_games = 0
game_tot = 0

while game_tot < 20:
    while I_points < 11 and O_points < 11 or abs(I_points - O_points) < 2:
        randnum = random.randint(0,100)
        if randnum < 60:
            I_points = I_points + 1
        else:     
            O_points = O_points + 1
    print("Score:"+str(I_points)+"-"+str(O_points))
    if I_points > O_points:
        I_games = I_games + 1
    else:
        O_games = O_games + 1
    game_tot = game_tot + 1
    I_points = 0
    O_points = 0
    
print(str(I_games)+" , "+str(O_games)) 