""" This file contains algorithm code to play the solitaire game aces up, also known as idiots delight. """

import random

def initializecards():
    cards = [
            {'name':'A♠','suite':'spades','rank':14},
            {'name':'2♠','suite':'spades','rank':2},
            {'name':'3♠','suite':'spades','rank':3},
            {'name':'4♠','suite':'spades','rank':4},
            {'name':'5♠','suite':'spades','rank':5},
            {'name':'6♠','suite':'spades','rank':6},
            {'name':'7♠','suite':'spades','rank':7},
            {'name':'8♠','suite':'spades','rank':8},
            {'name':'9♠','suite':'spades','rank':9},
            {'name':'10♠','suite':'spades','rank':10},
            {'name':'J♠','suite':'spades','rank':11},
            {'name':'Q♠','suite':'spades','rank':12},
            {'name':'K♠','suite':'spades','rank':13},
            {'name':'A♡','suite':'hearts','rank':14},
            {'name':'2♡','suite':'hearts','rank':2},
            {'name':'3♡','suite':'hearts','rank':3},
            {'name':'4♡','suite':'hearts','rank':4},
            {'name':'5♡','suite':'hearts','rank':5},
            {'name':'6♡','suite':'hearts','rank':6},
            {'name':'7♡','suite':'hearts','rank':7},
            {'name':'8♡','suite':'hearts','rank':8},
            {'name':'9♡','suite':'hearts','rank':9},
            {'name':'10♡','suite':'hearts','rank':10},
            {'name':'J♡','suite':'hearts','rank':11},
            {'name':'Q♡','suite':'hearts','rank':12},
            {'name':'K♡','suite':'hearts','rank':13},
            {'name':'A♣','suite':'clubs','rank':14},
            {'name':'2♣','suite':'clubs','rank':2},
            {'name':'3♣','suite':'clubs','rank':3},
            {'name':'4♣','suite':'clubs','rank':4},
            {'name':'5♣','suite':'clubs','rank':5},
            {'name':'6♣','suite':'clubs','rank':6},
            {'name':'7♣','suite':'clubs','rank':7},
            {'name':'8♣','suite':'clubs','rank':8},
            {'name':'9♣','suite':'clubs','rank':9},
            {'name':'10♣','suite':'clubs','rank':10},
            {'name':'J♣','suite':'clubs','rank':11},
            {'name':'Q♣','suite':'clubs','rank':12},
            {'name':'K♣','suite':'clubs','rank':13},
            {'name':'A♢','suite':'diamonds','rank':14},
            {'name':'2♢','suite':'diamonds','rank':2},
            {'name':'3♢','suite':'diamonds','rank':3},
            {'name':'4♢','suite':'diamonds','rank':4},
            {'name':'5♢','suite':'diamonds','rank':5},
            {'name':'6♢','suite':'diamonds','rank':6},
            {'name':'7♢','suite':'diamonds','rank':7},
            {'name':'8♢','suite':'diamonds','rank':8},
            {'name':'9♢','suite':'diamonds','rank':9},
            {'name':'10♢','suite':'diamonds','rank':10},
            {'name':'J♢','suite':'diamonds','rank':11},
            {'name':'Q♢','suite':'diamonds','rank':12},
            {'name':'K♢','suite':'diamonds','rank':13} 
            ]
    random.shuffle(cards)
    return(cards)

def deal(cards,tableau):

    for i in range(4):
        tableau[i].insert(0,cards.pop(0))
    displayTableau(tableau)
    return([tableau,cards]) 

def moveCard(position1, position2, tableau):
    position1 = int(position1)-1
    position2 = int(position2)-1
    a = [1,2,3,4]
    a.pop(0)
    if tableau[position2] == []:
        tableau[position2].insert(0,tableau[position1].pop(0))
    else:
        print('Invalid Move')
    displayTableau(tableau)
    return(tableau)

def removeCard(remove,tableau): 
    remove = int(remove)-1
    validMove = False
    for i in range(4):
        if remove != i:
            if tableau[i]:
                if tableau[remove][0]['suite'] == tableau[i][0]['suite']:
                    if tableau[remove][0]['rank'] < tableau[i][0]['rank']:
                        validMove = True
    if validMove == True:
        tableau[remove].pop(0)         
    else:
        print('Invalid Move')
    displayTableau(tableau)
    return(tableau)

def displayTableau(tableau):
    printcard = [[],[],[],[]] 
    for i in range(4):
        if tableau[i]:
            printcard[i] = tableau[i][0]['name']
        else:
            printcard[i] = '[]'
    print('{} {} {} {}'.format(printcard[0],printcard[1],printcard[2],printcard[3]))

def gamePlay():
    win = True 
    contGame = True
    tableau = [[],[],[],[]] 
    cards = initializecards()
    tableau,cards = deal(cards,tableau)
    while contGame == True:
        move = input("Remove a Card? ")
        if move == '1' or move == '2' or move =='3' or move == '4':
            tableau = removeCard(move,tableau)  
        if move == 'deal':
            if cards != []:
                tableau,cards = deal(cards,tableau)
            else:
                print('End of Deck')
                contGame = False
        if move == 'move':
            position1 = input("Card To Move? ")
            position2 = input("New Location? ")
            tableau = moveCard(position1,position2,tableau)
        if move == 'end game':
            contGame = False
    for i in range(4):
        if not tableau[i]:
            win = False
        elif tableau[i][0]['rank'] != 14 or len(tableau[i]) != 1:
            win = False 
    if win == True:
       displayTableau(tableau)
       print('Congragulations! You Won')
    if win == False:
        displayTableau(tableau)
        print('Better Luck Next Time')

if __name__ == '__main__':
    print('Welcome to Aces Up! \n New Game: start \n Remove a Card: 1 or 2 or 3 or 4 \n Move a Card: move \n Deal: deal \n Exit Game: end game')
    newGame = 'start'
    while newGame == 'start':
        gamePlay()
        newGame = input('New Game? ')
