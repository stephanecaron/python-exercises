import random
import sys
import time

cards = [['gb', 'rt', 'bt', 'wb'],
         ['rt', 'wt', 'bt', 'gt'],
         ['gt', 'gb', 'rb', 'bb'],
         ['rt', 'gt', 'wb', 'wt'],
         ['bb', 'wt', 'gb', 'rt'],
         ['rt', 'wb', 'bt', 'gb'],
         ['rb', 'gb', 'bb', 'wt'],
         ['rt', 'wb', 'bt', 'gt'],
         ['rb', 'gt', 'bb', 'wt']] 

cards_for_instant_solution = [['rt', 'rt', 'rt', 'rt'],
                               ['rb', 'rb', 'rb', 'rb'],
                               ['rt', 'rt', 'rt', 'rt'],
                               ['rb', 'rb', 'rb', 'rb'],
                               ['rt', 'rt', 'rt', 'rt'],
                               ['rb', 'rb', 'rb', 'rb'],
                               ['rt', 'rt', 'rt', 'rt'],
                               ['rb', 'rb', 'rb', 'rb'],
                               ['rt', 'rt', 'rt', 'rt']]

colas_cards = [['gt','rt','bb','yb'],
               ['gb','rt','yt','bb'],
               ['bb','gt','yt','rb'],
               ['rb','gt','bt','yb'],
               ['yb','rt','bt','gb'],
               ['yb','rt','bt','rb'],
               ['gt','yt','rb','bb'],
               ['bb','gt','yt','gb'],
               ['bb','rt','yt','gb']]





def check_neighbor(side, comparedSide):
    if side[0] != comparedSide[0]:
        return False
    if side[1] == comparedSide[1]:
        return False
    return True


def check_neighbors(card, currentIndex, randomizedArray):
    if currentIndex > 2:
        north = card[0]
        northCardIndex = currentIndex - 3
        northCard = randomizedArray[northCardIndex]
        if not check_neighbor(north, northCard[2]):
            return False
    if (currentIndex + 1) % 3 != 0:
        east = card[1]
        eastCardIndex = currentIndex + 1
        eastCard = randomizedArray[eastCardIndex]
        if not check_neighbor(east, eastCard[3]):
            return False
    if currentIndex < 6:
        south = card[2]
        southCardIndex = currentIndex + 3
        southCard = randomizedArray[southCardIndex]
        if not check_neighbor(south, southCard[0]):
            return False
    if currentIndex % 3 != 0:
        west = card[3]
        westCardIndex = currentIndex - 1
        westCard = randomizedArray[westCardIndex]
        if not check_neighbor(west, westCard[1]):
            return False
    return True


def randomizeArray(cards): # tested, works
    pickedCards = []
    randomizedArray = []
    while len(randomizedArray) < 9:
        currentCardNumber = random.randint(0, 8)
        if currentCardNumber not in pickedCards:
            currentCard = cards[currentCardNumber]
            pickedCards.append(currentCardNumber)
            randomSideFlip = random.randint(0, 3)
            for _ in range(randomSideFlip):
                currentCard = currentCard[1:] + [currentCard[0]]
            randomizedArray.append(currentCard)
    return randomizedArray


def solver(cards):
    checkCount = 0
    foundAnswer = False
    update_interval = 10  # Adjust this value based on your preference

    while not foundAnswer:
        randomizedArray = randomizeArray(cards)
        currentIndex = 0
        for card in randomizedArray:
            if not check_neighbors(card, currentIndex, randomizedArray):
                foundAnswer = False
                break
            currentIndex += 1
        else:
            foundAnswer = True

        checkCount += 1

        # Print update every N iterations
        if checkCount % update_interval == 0:
            sys.stdout.write(f'\rCurrent checkCount: {checkCount}')
            sys.stdout.flush()

    if foundAnswer:
        print(f'\nFound the answer in {checkCount} attempts')
        print(randomizedArray)
    else:
        print(f'\nUnable to find a valid solution in {checkCount} attempts')
    return randomizedArray


solver(colas_cards)