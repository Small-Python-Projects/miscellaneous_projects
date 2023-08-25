import random

I_points = 0
O_points = 0

I_games = 0
O_games = 0

I_matches = 0
O_matches = 0

game_tot = 0
serve = True

while game_tot < 20:
    while I_points < 9 and O_points < 9 or abs(I_points - O_points) < 2:
        randnum = random.randint(0,100)
        if randnum < 60:
            if serve == True:
                I_points = I_points + 1
            else:
                serve = True   
        else:     
            if serve == False:
                O_points = O_points + 1
            else:
                serve = False
    print("Score:"+str(I_points)+"-"+str(O_points))
    if I_points > O_points:
        I_games = I_games + 1
    else:
        O_games = O_games + 1
        
    I_points = 0
    O_points = 0
    game_tot = game_tot + 1
    serve = True
print(str(I_games)+', '+str(O_games))
