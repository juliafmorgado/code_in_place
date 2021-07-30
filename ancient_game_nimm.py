"""
The game of Nimm goes as follows:
+ The game starts with a pile of 20 stones between the players.
+ The two players alternate turns.
+ On a given turn, a player may take either 1 or 2 stone from the center pile.
+ The two players continue until the center pile has run out of stones.
+ The last player to take a stone loses. 
"""

import random
SET_PLAYER = random.randint(0,1)

def main():
    #Who starts the game? 
    #set a variable 'turns' to keep track of who's turn it is and who's winning.
    if SET_PLAYER == 0:
        print("Player 1, you can start the game!")
        turns = 0
    else :
        print("Player 2, you can start the game!")
        turns = 1
    print()
    #set a variable 'stones', we always start with 20 stones.
    stones = 20
    while stones > 0:
        print("There are ", stones, "stones left")
        #define first who's turn it is, then ask the question "would you like to remove 1 or 2 stones?".
        if turns % 2 == 0: #if the turns variable is even, it's Player 1 turn to play
            player = "Player 1 "
            #ask Player 1 "would you like to remove 1 or 2 stones?", put answer in variable one_or_two
            one_or_two = int(input(player + "would you like to remove 1 or 2 stones? "))
            #check if answer is valid
            while one_or_two > 2:
                one_or_two = int(input("Please enter 1 or 2: "))
            print()
        else :
            player = "Player 2 "
            one_or_two = random.randint(1,2)
            #ask Player 2 "would you like to remove 1 or 2 stones?", put answer in variable one_or_two
            print(player, "would you like to remove 1 or 2 stones?", one_or_two)
            print()
        #set how many stones are left over & update turns
        stones = stones - one_or_two
        turns = turns + 1
    print("Game over")
    print()
    #who wins? The last player to take a stone loses!
    if turns % 2 == 0: #value turns is even, this means last player was player 2.
        print("You won Player 1, FINISH HIM!")
    else :
        print("Player 2 wins! Player 1, you are a real Nimmbicil!")

if __name__ == '__main__':
    main()