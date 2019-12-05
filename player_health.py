#!/usr/bin/python/
player_health=200
print('player health check')
print('current player health standing at: ') + str(player_health)

print('player is encountering danger and in danger of getting stabbed. Take cover quickly.')
stab = -1
#poisonus damagae decreases health for 5, max of 20

#ok this while need something called a "for loop"
#once hit with poisonus stab, decresase player health by 5 points until 20 points are decreased
#I'll go back to see how to code it

injury = player_health + 20*stab

print injury
