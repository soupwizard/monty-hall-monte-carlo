import random

# setup

class MontyHall():

    def run_once(self):

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

        #
        ### Case where player switches
        #
        # player picks other door left in doors
        if doors[0] == player_door:
            player_new_door = doors[1]
        elif doors[1] == player_door:
            player_new_door = doors[0]
        #print('player switched to door', player_new_door)

        # Did player win?
        if player_new_door == prize_door:
            player_switched_and_won = True
        else:
            player_switched_and_won = False
        #print('Player switched and won: %s' % (player_switched_and_won))

        #
        ### Case where player doesn't switch
        #
        # player keeps their first choice

        #print('player keeps door', player_door)

        # Did player win?
        if player_door == prize_door:
            player_not_switched_and_won = True
        else:
            player_not_switched_and_won = False
        #print('Player not switched and won: %s' % (player_not_switched_and_won))

        return player_switched_and_won, player_not_switched_and_won

def run_monty(iterations):
    mh = MontyHall()

    count = 0 
    player_switched_and_won_total     = 0
    player_not_switched_and_won_total = 0
    for x in range(0,iterations):
        count += 1
        player_switched_and_won, player_not_switched_and_won = mh.run_once() 
        if player_switched_and_won: player_switched_and_won_total += 1
        if player_not_switched_and_won: player_not_switched_and_won_total += 1

    print ("Didn't switch : count: %d, won: %.2f%%" % (count, (player_not_switched_and_won_total/count)*100))
    print ("Always switch : count: %d, won: %.2f%%" % (count, (player_switched_and_won_total/count)*100))

if __name__ == "__main__":
    run_monty(1000000)
