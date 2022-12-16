import random, argparse, sys
from multiprocessing import Pool

def run_monty_hall_game_once(game_id):

    #print('Game #%d' % (game_id))
    #sys.stdout.flush()

    doors = [0, 1, 2]
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

    return game_id, player_switched_and_won, player_not_switched_and_won

def run_monty(iterations, num_processes=6):

    count = 0 
    player_switched_and_won_total     = 0
    player_not_switched_and_won_total = 0

    '''
    # single-process
    for x in range(0,iterations):
        count += 1
        game_id, player_switched_and_won, player_not_switched_and_won = run_monty_hall_game_once(count) 
        if player_switched_and_won: player_switched_and_won_total += 1
        if player_not_switched_and_won: player_not_switched_and_won_total += 1

    '''
    # multi-process
    game_ids = [*range(1, iterations+1)]
    with Pool(num_processes) as pool:
        results = pool.imap_unordered(run_monty_hall_game_once, game_ids)
        for game_id, player_switched_and_won, player_not_switched_and_won in results:
            count += 1
            if player_switched_and_won: player_switched_and_won_total += 1
            if player_not_switched_and_won: player_not_switched_and_won_total += 1

    print ("Didn't switch: won: %.4f%%" % ((player_not_switched_and_won_total/count)*100))
    print ("Always switch: won: %.4f%%" % ((player_switched_and_won_total/count)*100))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--runs", type=int, default=100000, help="Number of runs for simulation")
    parser.add_argument("-p", "--processes", type=int, default=6, help="Number of processes to use to run simulation")
    args = parser.parse_args()

    print()
    print(f"Running Monty Hall Monte Carlo simulation {args.runs:,} times")
    run_monty(args.runs, args.processes)
    print()
