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


def choosePlayer(number: str, size: int) -> int:
    """Return a player selected by the user

    :param number: The number of the player
    :param size: The number of different player playable
    :return:
    """
    print('--> Choose player ' + number + ':')
    player = int(input())
    while player < 0 or player >= size:
        print("You should enter a number between 0 and " + str(size - 1))
        player = int(input())
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
    print("Turn {} :".format(i+1))
    player1.play()
    player2.play()
    gain(player1, player2)


def gain(p1: Player, p2: Player):
    """Give gain to each player with their last turn decision

    :param p1: Player 1
    :param p2: Player 2
    :return: None
    """
    if p1.choice[-1] == p2.choice[-1] == "C":
        p1.score += 3
        p2.score += 3
    elif p1.choice[-1] == p2.choice[-1] == "B":
        p1.score += 0
        p2.score += 0
    elif p1.choice[-1] == "C":
        p1.score += -1
        p2.score += 3
    else:
        p1.score += 3
        p2.score += -1


def main():
    players = [AllCheat(), AllCooperate(), Copycat(), Detective(), Grudger()]
    sizePlayers = len(players)
    num_turn = 0
    max_num_turn = 10

    for i in range(sizePlayers):
        print(i, "- {}".format(players[i]))

    player1 = choosePlayer("1", sizePlayers)
    player2 = choosePlayer("2", sizePlayers)

    while num_turn < max_num_turn:
        turn(player1, player2, num_turn)
        num_turn += 1


main()
