from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            #print("Go North!")
            player.move_north()
        elif action_input in ['s', 'S']:
            #print("Go South!")
            player.move_south()
        elif action_input in ['e', 'E']:
            #print("Go East!")
            player.move_east()
        elif action_input in ['w', 'W']:
            #print("Go West!")
            player.move_west()
        elif action_input in ['i', 'I']:
            player.print_inverntory()

def get_player_command():
    return input('Action: ')

play()

