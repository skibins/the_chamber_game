# Import necessary modules and classes
from player import Player
from boss import Boss
import elixirs_info
import rooms_info
import chests_info

# Import necessary libraries
import time
import os
import pygame

# Set the starting room
start_room = rooms_info.rooms[rooms_info.current_room]


# Function to play background music
def play_music(file_name, loop=True):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), file_name))
    pygame.mixer.music.play(loops=-1 if loop else 0)


# Function to travel through rooms
def travel(actual_room):
    print(actual_room)

    # Check if the current room is the boss room
    if rooms_info.current_room == 'room_boss':
        enter_boss_fight()
    else:
        # Check if the player has entered the room before
        if rooms_info.current_room not in rooms_info.rooms_entered:
            print(chests_info.check_room())
            player.gold = sum(chests_info.gained_gold_amounts)
            print(f'You have: \033[93m{player.gold}\033[0m gold')
            rooms_info.rooms_entered.append(rooms_info.current_room)

        # Check if the player is in a special room
        if rooms_info.current_room == 'room_right_top':
            enter_shop()

        if rooms_info.current_room == 'cool_room':
            print(f'You\'ve found the \033[93mcool room\033[0m!')

        correct_direction = False

        # Loop to ensure correct direction input
        while not correct_direction:
            travel_path = input('Where do you want to go? ')
            if travel_path in rooms_info.rooms_paths[rooms_info.current_room]:
                correct_direction = True
                rooms_info.current_room = rooms_info.rooms_paths[rooms_info.current_room][travel_path]
                travel(rooms_info.rooms[rooms_info.current_room])
            else:
                print("You can't go that way!")


# Function to enter the shop
def enter_shop():
    print('\033[96mYou entered the shop\033[0m')
    want_to_buy = input('If you want to buy some elixirs type "buy". If not - hit enter. ')
    if want_to_buy == 'buy':
        print(f'You have \033[93m{player.gold}\033[0m gold.')
        for key in elixirs_info.elixirs:
            print(f'MAGIC ELIXIR NAME: \033[91m{key}\033[0m, Elixir price: {elixirs_info.elixirs[key]['price']}')

        elixir_name = input('Type elixir name or hit enter to leave the shop. ')
        if elixir_name in elixirs_info.elixirs:
            elixir_price = elixirs_info.elixirs[elixir_name]['price']
            if player.gold >= elixir_price:
                player.gold -= elixir_price
                if 'damage' in elixirs_info.elixirs[elixir_name]:
                    player.damage += elixirs_info.elixirs[elixir_name]['damage']
                if 'health' in elixirs_info.elixirs[elixir_name]:
                    player.health += elixirs_info.elixirs[elixir_name]['health']

                print('Your stats:')
                print(f'Damage: \033[93m{player.damage}\033[0m')
                print(f'Health: \033[92m{player.health}\033[0m')
            else:
                print('\033[91mNot enough gold.\033[0m')

    print('You left the shop...')


# Function to enter the boss fight
def enter_boss_fight():
    play_music('music/boss_fight.wav', loop=True)
    boss = Boss()
    print(f'\033[93m{player.name.upper()}, YOU ENTERED THE BOSS LAIR\033[0m')
    print('\033[95mTHERE IS NO ESCAPE NOW! YOU HAVE TO FIGHT\033[0m')
    print('Your stats:')
    print(f'Damage: \033[93m{player.damage}\033[0m')
    print(f'Health: \033[92m{player.health}\033[0m')
    print('Boss stats:')
    print(f'Damage: \033[93m{boss.damage}\033[0m')
    print(f'Health: \033[92m{boss.health}\033[0m')

    start_fight = input('Type "FIGHT" to start the fight. ')
    if start_fight == 'FIGHT' or start_fight == 'fight':
        fight_boss(boss)


# Function to simulate the boss fight
def fight_boss(boss):
    end_game_message = ''
    lowest_hp = min(player.health, boss.health)

    while lowest_hp > 1:
        print('\033[95mYou hit the Boss!\033[0m')
        boss.health = boss.health - player.damage
        print(f'{player.name} hp: {player.health}.')
        print(f'Boss hp: {boss.health}.')

        if min(player.health, boss.health) <= 0:
            break

        time.sleep(2)

        print('\033[93mBoss hits You!\033[0m')
        player.health = player.health - boss.damage
        print(f'{player.name} hp: {player.health}.')
        print(f'Boss hp: {boss.health}.')

        time.sleep(2)

        lowest_hp = min(player.health, boss.health)

    if player.health > boss.health:
        end_game_message = """==============================================================
\033[96mCongratulations {0}! You defeated the Boss and won the game!\033[0m
=============================================================="""

    else:
        end_game_message = """================================================
\033[91mUnfortunately {0} got defeated by the Boss...\033[0m
================================================"""

    print(end_game_message.format(player.name))
    time.sleep(15)


# Main function
if __name__ == '__main__':
    print(
        """|======================|
|\033[96mWELCOME TO THE CHAMBER\033[0m|
|======================|""")

    print(
        """You are a warrior whose mission is to explore this majestic abandoned dungeon.
There are thousands of gold here.
But be careful...
Some creatures are not willing to let you out with all this gold.
""")

    print("""\033[93mType 'up' / 'down' / 'left' / 'right' to travel through rooms.
The map is 3x3.\033[0m
        """)

    start = input('Type "START" to enter the game... ')

    if start == 'START' or start == 'start':
        player_name = input('Enter your name: ')
        player = Player(player_name)
        play_music('music/travel_music.wav', loop=True)
        travel(start_room)
    else:
        print('Exiting...')
        exit()
