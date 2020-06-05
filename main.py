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
from players.copykitten import Copykitten
from players.gradual import Gradual
from players.simpleton import Simpleton

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
    elif player == 5:
        player = Copykitten()
    elif player == 6:
        player = Gradual()
    elif player == 7:
        player = Simpleton()    
    return player


def turn(player1: Player, player2: Player, i: int, mistakeRate: int):
    """Play one turn between two player

    :param player1: Player 1
    :param player2: Player 2
    :param i: The number of the turn
    :return: None
    """
    print("Turn {} : ".format(i+1), end="")
    if i == 0:
        player1.play('C', mistakeRate)
        player2.play('C', mistakeRate)
    else :
        player1.play(player2.choice[-1], mistakeRate)
        player2.play(player1.choice[-2], mistakeRate)
    print("Player 1 [{}] || Player 2 [{}]".format(player1.choice[-1],player2.choice[-1]))
    gain(player1, player2)

def fastTurn(player1: Player, player2 : Player, max_turn : int, mistakeRate: int):
    """Play all the turns between two player without printing trace

    :param player1: Player 1
    :param player2: Player 2
    :param max_turn: The number of turn of a confrontation

    :return: None
    """
    n = 0
    while n < max_turn :
        if n == 0:
            player1.play('C', mistakeRate)
            player2.play('C', mistakeRate)
        else :
            player1.play(player2.choice[-1], mistakeRate)
            player2.play(player1.choice[-2], mistakeRate)    
        gain(player1, player2, False)
        n+= 1

    print("Player", player1.name, ":", player1.get_score(), "\nPlayer {} : {}\n".format(player2.name, player2.get_score()))
    # Empty the players' list of choice for next match
    player1.reset()
    player2.reset()


def gain(p1: Player, p2: Player, printTrace=True):
    """Give gain to each player with their last turn decision

    :param p1: Player 1
    :param p2: Player 2
    :return: None
    """
    if p1.choice[-1] == p2.choice[-1] == "C":
        if printTrace :
            print("Player 1 [+2] || Player 2 [+2]\n")

        p1.set_score(p1.get_score() + 2)
        p2.set_score(p2.get_score() + 2)
    elif p1.choice[-1] == p2.choice[-1] == "B":
        if printTrace :
            print("Player 1 [+0] || Player 2 [+0]\n")

    elif p1.choice[-1] == "C":
        if printTrace :
            print("Player 1 [-1] || Player 2 [+3]\n")

        p1.set_score(p1.get_score() - 1)
        p2.set_score(p2.get_score() + 3)
    else:
        if printTrace :
            print("Player 1 [+3] || Player 2 [-1]\n")

        p1.set_score(p1.get_score() + 3)
        p2.set_score(p2.get_score() - 1)

def chooseMode() -> int:
    """Choose the application's mode that will be executed 

    :return:    0 for one-on-one
                1 for tournament
                2 for ecological competition
    """
    print("\nChoose the mode you want to play :\n\n\t0. One-on-one\n\n\t1. Simple tournament : Choose the number of player and their repartition, then each one will do a one-on-one with all the others\n\n\t2. Ecological competition : Multiple tournament where the 20% better players are replicated and 20% worst are eliminated at the end of each tournament.\n\n\n Enter 0, 1 or 2")
    return checkIntInput(0, 2)

def checkIntInput(min : int, max : int):
    """Get the input then return it only if it is between the 2 arguments
    
    :param min: the minimum for the value 
    :param max: the maximum for the value 

    :return: a valid value of the input 
    """
    
    var = -1
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

def playTournament(playersList : list,  max_num_turn : int, mistake_rate: int):
    """ Make all the players in playersList have a one-on-one with each other to carry on a tournament

    :param playersList : The list containing all the tournament's player
    :param max_num_turn : The number of turn of each match
    :param mistake_rate : The number (in pourcentage) of chance for the player to do the opposite they want to

    :return: none
    """
    i = len(playersList)
    while i > 1:
        i -= 1
        tmpList = playersList[:i]
        for p in tmpList :
            fastTurn(playersList[i], p, max_num_turn, mistake_rate)

    
    playersList.sort(key = Player.get_score)
    print("\nResults of tournament :\n")
    i = 0
    for p in playersList :
        print("Player ", i + 1, "(", p.name, ") : ", p.get_score())
        i += 1

def updatePopulation(playersList : list):
    length = len(playersList) - 1
    for i in range(int(length / 5)):
        playersList[i] = type(playersList[length - i])()

    for p in playersList :
        p.set_score(0)


def main():
    isEndOfGame = False
    players = [AllCheat(), AllCooperate(), Copycat(), Detective(), Grudger(), Copykitten(), Gradual(), Simpleton()]
    sizePlayers = len(players)
    num_turn = 0
    print("Welcome to this simulation of the prisonner's game\n\nLet's begin with our players :")
    while not isEndOfGame :
        print("How many turn per match do you want ? ")
        max_num_turn = checkIntInput(1, 50)
        print("How high you want the chance of mistakes to be (in %) ?")
        mistake_rate = checkIntInput(0, 50)
        for i in range(sizePlayers):
            print(i, "- {}".format(players[i]))
        mode = chooseMode()
        if mode == 0 : # one-on-one
            player1 = choosePlayer(sizePlayers, "1")
            player2 = choosePlayer(sizePlayers, "2")

            while num_turn < max_num_turn:
                turn(player1, player2, num_turn, mistake_rate)
                num_turn += 1

            print("Player 1 (", player1.name, ") got a score of {}\nPlayer 2 (".format(player1.get_score()), player2.name, ") got a score of {}\n".format(player2.get_score()))
        else : # tournament
            playersList = chooseListOfPlayer(players)
            if mode == 1 :
                print("\nStart of Tournament : \n")
                playTournament(playersList, max_num_turn, mistake_rate)
            else : # Ecological competition
                print("\nStart of Ecological competition :\n")
                mustEnd = False
                while(not mustEnd) :
                    playTournament(playersList, max_num_turn, mistake_rate)
                    updatePopulation(playersList)
                    print("\nDo you wish to continue ? (y/n)\n")
                    choice = input()
                    if choice != 'n' and choice != 'y':
                        print("\nPlease enter y or n\n")
                    elif choice == 'n' :
                        mustEnd = True

        print("\nYou can quit with q, or start again with any other key")  
        if input() == 'q' :
            isEndOfGame = True
        num_turn = 0

main()
