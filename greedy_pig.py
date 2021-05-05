#   Bård Eilertsen 05.05.2021
#   Looking for the optimal strategy for greedy pig.
#   One dice
#   Point strategy og throw strategy
#   Simulate how many rounds it takes to retch a point value

import random

goal_value = 100
dice_throw_per_round = 20
rounds_of_simulations = 100000
dice_value = random.randint(1, 6)
rounds_counter = 0
points_round = 0
points_total = 0
rounds_to_reach_goal_value = [[0 for i in range(dice_throw_per_round)] for j in range(rounds_of_simulations)] # This is the information I need.

print ("Goal= ", goal_value, " points")
#print ("Dice= ", dice_value)

for s in range(0, rounds_of_simulations):
    for n in range(1,dice_throw_per_round+1):
        points_total = 0
        print("Throw the dice", n,"times per round")
        while (goal_value > points_total):
            points_round = 0
            rounds_counter = rounds_counter+1
            #print ("New Round ------------------")
            #print ("Points total = ", points_total)
            #print ("Rounds counter = ", rounds_counter)
            for m in range(0,n):
                dice_value = random.randint(1, 6)
                #print ("Dice= ", dice_value)
                if (dice_value <= 1):
                    #print("Dice value 1. No points this round ")
                    points_round = 0
                    break
                else:
                    points_round = points_round + dice_value
            points_total = points_total + points_round
            if (points_total >= goal_value):
                print("Winner!")
                print ("Points total= ", points_total)
                rounds_to_reach_goal_value[s][n-1] = rounds_counter
                rounds_counter = 0
                continue
    
for i in range(rounds_of_simulations):   
    print (rounds_to_reach_goal_value[i])
    
print ("[1,2,3,4,5,6,7,8,9,10]")
print ([float(sum(l))/len(l) for l in zip(*rounds_to_reach_goal_value)])
  
input("Press Enter to continue...")