"""
Le dilemme du prisonnier
@author: fabian devel - medhi louison - lucas cosson
"""
from players.player import Player
from players.allcheat import AllCheat
from players.allcooperate import AllCooperate
from players.copycat import Copycat
from players.detective import Detective
from players.grudger import Grudger


def choosePlayer(size: int, number = "") -> Player:
    """Return a player selected by the user

    :param number: The number of the player
    :param size: The number of different player playable
    :return:
    """
    if number != "":
        print('--> Choose player ' + number + ':')
        player = checkIntInput(0, size - 1)
    else :
        player = size

    if player == 0:
        player = AllCheat()
    elif player == 1:
        player = AllCooperate()
    elif player == 2:
        player = Copycat()
    elif player == 3:
        player = Detective()
    elif player == 4:
        player = Grudger()
    return player


def turn(player1: Player, player2: Player, i: int):
    """Play one turn between two player

    :param player1: Player 1
    :param player2: Player 2
    :param i: The number of the turn
    :return: None
    """
    print("Turn {} : ".format(i+1), end="")
    if i == 0:
        player1.play('C')
        player2.play('C')
    else :
        player1.play(player2.choice[-1])
        player2.play(player1.choice[-1])
    print("Player 1 [{}] || Player 2 [{}]".format(player1.choice[-1],player2.choice[-1]))
    gain(player1, player2)

def fastTurn(player1: Player, player2 : Player, max_turn : int):
    """Play all the turns between two player without printing trace

    :param player1: Player 1
    :param player2: Player 2
    :param max_turn: The number of turn of a confrontation

    :return: None
    """
    n = 0
    while n < max_turn :
        if n == 0:
            player1.play('C')
            player2.play('C')
        else :
            player1.play(player2.choice[-1])
            player2.play(player1.choice[-1])    
        gain(player1, player2, False)
        n+= 1

    print("Player 1 (", player1.name, ") : ", player1.get_score(), "\nPlayer 2 (", player2.name, ") : {}\n".format(player2.get_score()))


def gain(p1: Player, p2: Player, printTrace=True):
    """Give gain to each player with their last turn decision

    :param p1: Player 1
    :param p2: Player 2
    :return: None
    """
    if p1.choice[-1] == p2.choice[-1] == "C":
        if printTrace :
            print("Player 1 [+2] || Player 2 [+2]\n")

        p1.set_score(2)
        p2.set_score(2)
    elif p1.choice[-1] == p2.choice[-1] == "B":
        if printTrace :
            print("Player 1 [+0] || Player 2 [+0]\n")

        p1.set_score(0)
        p2.set_score(0)
    elif p1.choice[-1] == "C":
        if printTrace :
            print("Player 1 [-1] || Player 2 [+3]\n")

        p1.set_score(-1)
        p2.set_score(3)
    else:
        if printTrace :
            print("Player 1 [+3] || Player 2 [-1]\n")

        p1.set_score(3)
        p2.set_score(-1)

def chooseMode() -> int:
    """Choose the application's mode that will be executed 

    :return:    0 for one-on-one
                1 for tournament
    """
    print("\nDo you want to play a tournament or a one-on-one (enter 't' for tournament, anything else for a one-one-one")
    if input() == 't':
        return 1
    return 0

def checkIntInput(min : int, max : int):
    """Get the input then return it only if it is between the 2 arguments
    
    :param min: the minimum for the value 
    :param max: the maximum for the value 

    :return: a valid value of the input 
    """
    
    var = -1
    print("max : ", max)
    while var < min or var > max :
        try:
            var = int(input())
        except ValueError:
            print('Please enter an integer between', min, 'and', max)
            
    return var

def chooseListOfPlayer(players : list()) -> list():
    """ Ask to the user how many and which players he wants for the tournament

    :param players: the list of the possible players

    :return: a list with the right number of players to do the tournament
    """
    playerList = list()
    print("How many players do you want ?")
    nbPlayer = checkIntInput(2, 50)
    sizeLeft = nbPlayer
    stopLoop = False
    
    while not stopLoop :
        for p in players :
            print("How many", p.name, "do you want ?")
            tmpNb = checkIntInput(0, sizeLeft)
            print("tmpNb:{} index: {} sizeleft : {}".format(tmpNb, players.index(p), sizeLeft))
            tmpList = list()
            for i in range(tmpNb):
                tmpList.append(choosePlayer(players.index(p)))
            playerList.extend(tmpList)
            sizeLeft = nbPlayer - len(playerList)
            if sizeLeft == 0 :
                print("All player attributed")
                return playerList
            else :
                print(sizeLeft, "players left")
        if sizeLeft > 0 :
            print("You still have ", sizeLeft, "players available\nDo you want to assign them ? (y/n)")
            if input() != 'y' :
                stopLoop = True

    return playerList

def main():
    isEndOfGame = False
    players = [AllCheat(), AllCooperate(), Copycat(), Detective(), Grudger()]
    sizePlayers = len(players)
    num_turn = 0
    print("Welcome to this simulation of the prisonner's game\n\nLet's begin with our players :")
    while not isEndOfGame :
        print("How many turn per match do you want ? ")
        max_num_turn = checkIntInput(1, 20)
        for i in range(sizePlayers):
            print(i, "- {}".format(players[i]))
        
        mode = chooseMode()
        if mode == 0 :
            player1 = choosePlayer(sizePlayers, "1")
            player2 = choosePlayer(sizePlayers, "2")

            while num_turn < max_num_turn:
                turn(player1, player2, num_turn)
                num_turn += 1

            print("Player 1 (", player1.name, ") got a score of {}\nPlayer 2 (".format(player1.get_score()), player2.name, ") got a score of {}\n".format(player2.get_score()))
        else :
            playersList = chooseListOfPlayer(players)
            print("\nStart of Tournament : \n")
            i = len(playersList)
            while i > 1:
                i -= 1
                tmpList = playersList[:i]
                for p in tmpList :
                    fastTurn(playersList[i], p, max_num_turn)
                
            print("\nResults of tournament :\n")
            i = 0
            for p in playersList :
                print("Player ", i + 1, "(", p.name, ") : ", p.get_score())
                i += 1

        print("\nYou can quit with q, or start again with any other key")  
        if input() == 'q' :
            isEndOfGame = True
        num_turn = 0

main()
