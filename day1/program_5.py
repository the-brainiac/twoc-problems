score1 = int(input('Score of first player:'))
score2 = int(input('Score of second player:'))
score3 = int(input('Score of third player:'))
strike_rate1 = (score1/60)*100
strike_rate2 = (score2/60)*100
strike_rate3 = (score3/60)*100

print('strike rates are :',strike_rate1,strike_rate2,strike_rate3)

"""
	To calculate the runs
	run = (strike rate/100)*number of balls
	since the number of balls are 2 times run will also be 2 times
"""
print('Run scored by player 1 after 60 more balls:',score1*2)
print('Run scored by player 2 after 60 more balls:',score2*2)
print('Run scored by player 3 after 60 more balls:',score3*2)

#if a player only scored his score by sixes this will be the only case when maximum six we get

print("Maximum number of sixes by player 1:", score1//6)
print("Maximum number of sixes by player 2:", score2//6)
print("Maximum number of sixes by player 3:", score3//6)
