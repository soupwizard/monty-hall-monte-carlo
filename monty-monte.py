import random

# setup

class MontyHall():

    def run_once(self, player_switch):
        player_win    = None

        #print()
        #print('-----------------------')
        #print()

        doors = [0, 1, 2]
        #print('doors', doors)
        prize_door = random.randint(0,2)
        #print('prize', prize_door)

        # phase 1: player picks a door
        player_door = random.randint(0,2)
        #print('player', player_door)

        # phase 2: monty opens 1 of remaining doors
        # monty picks first non-prize, non-player door
        monty_pick = None
        for x in range(0,3):
            #print('Prize: %d, Player: %d, x: %d, Doors %s' % (prize_door, player_door, x, doors) )
            if doors[x] == prize_door:
                #print ('cant pick prize door', x)
                continue
            elif doors[x] == player_door:
                #print ('cant pick player door', x)
                continue
            else:
                monty_pick = x
                #print('monty picked', monty_pick)
                break

        # remove monty's door from door choices
        doors.pop(monty_pick)
        #print('remaining doors', doors)

        # player decides to swwitch or not 
        if player_switch:
            # player picks other door left in doors
            if doors[0] == player_door:
                player_door = doors[1]
            elif doors[1] == player_door:
                player_door = doors[0]
            #print('player switched to door', player_door)
        else:
            # player keeps their first choice
            #print('player keeps door', player_door)
            pass

        # Did player win?
        if player_door == prize_door:
            player_won = True
        else:
            player_won = False
        #print('Player won: %s' % (player_won))

        return player_switch, player_won

    def run(self, num_times):
        pass


mh = MontyHall()

count = 0 
player_won_count = 0
for x in range(0,1000000):
    count += 1
    player_switch, player_won = mh.run_once(False) 
    if player_won: player_won_count += 1

print ('Doesnt switch: count: %d, won: %.2f' % (count, player_won_count/count))

count = 0 
player_won_count = 0
for x in range(0,1000000):
    count += 1
    player_switch, player_won = mh.run_once(True) 
    if player_won: player_won_count += 1

print ('Always switch: count: %d, won: %.2f' % (count, player_won_count/count))


