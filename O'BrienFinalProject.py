import time

def displayIntro():
    print('You are in search of a rare sword.')
    time.sleep(2)
    print('You hear rumors it is in a cave nearby.')
    time.sleep(2)
    print('Upon entering the cave you see a rusty old sword on the ground.')
    time.sleep(2)
    print('Do you want to pick it up? Something is better than nothing, right?')
    time.sleep(2)
    print()

def pickUpSword():
    sword = ''
    while sword != '1' and sword != '2':
        print('Pick up the sword? (1 for yes, 2 for no)')
        sword = input()

    return sword

def chooseSword():
    print(' ')
    time.sleep(2)
    print('You venture further into the cave.')
    time.sleep(2)
    print('You find two identical swords. One is real and one is fake. Choose wisely!')
    time.sleep(2)
    print('The fake is known to be cursed and may kill you!')
    time.sleep(2)
    sword = ''
    while sword != '1' and sword != '2':
        print('Pick up which sword? (1 or 2)')
        sword = input()

    return sword

def fight(chosenCave):
    print('You go further into the cave.')
    time.sleep(2)
    print('A spider drops from the ceiling and attacks you!')
    time.sleep(2)
    print('You attempt to fight it off!')
    print()
    time.sleep(2)

    sword = 1
    

    if chosenCave == str(sword):
         print('You attack with your sword and narrowly kill the spider')
    else:
         print('You attempt to squish the giant spider with your hands. The spider kills you!')

def checkSword(swordNumber):
    randomSword = 1
    if swordNumber == str(randomSword):
         print('You picked the right sword! You are the best!')
         return swordNumber
    else:
         print('You picked the wrong sword! You died!*loser*')

def endingDialog():
    print(' ')
    time.sleep(2)
    print('Upon leaving with the sword, you encounter a stranger.')
    time.sleep(2)
    print('He asks for the sword and claims to be the rightful owner.')
    time.sleep(2)
    print('He offers a reward for the return of his sword.')
    time.sleep(2)
    print('Return the sword? (1 for yes, 2 for no)')
    
def giveSword():
    sword = input()
    if sword == '1':
         print('You agree to return the sword, the stranger gives you a larger sum of coins!')
         print('You live out the rest of your days in wealth living off the swords reward money!')
         return sword
    else:
         print('You keep the sword for yourself!')
         print('He summons a stone golem to attack you for the sword!')
         return sword

def golemAttacks():
    print(' ')
    time.sleep(2)
    print('A giant stone golem appears! He wants the sword for his master!')
    time.sleep(2)
    print('Attack or run? (1 for attack and 2 for run)')

def end():
    time.sleep(2)
    attack = input()
    if attack == '1':
        print('you attack the Golem!')
        time.sleep(2)
        print('Your attacks are useless against him!')
        time.sleep(2)
        print('He is made out of stone, what did you expect?')
        time.sleep(2)
        print('You died the way you lived, reckless!')
    else:
        print('You run away and live to fight another day.')
        time.sleep(2)
        print('You have found the sword and managed to keep it.')
        time.sleep(2)
        print('You win, yay!')
    


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    sword = pickUpSword()

    fight(sword)

    if sword == '1':
        swordNumber = chooseSword()
        realsword = checkSword(swordNumber)
        if realsword == '1':
            endingDialog()
            keptSword = giveSword()
            if keptSword == '2':
                attack = golemAttacks()
                end()
                
            

    print('Do you want to play again? (yes or no)')
    playAgain = input()

