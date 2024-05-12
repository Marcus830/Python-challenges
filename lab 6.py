import random
User = int(input("Enter an integer to seed the random number generator: "))


Players1_score = 0
Players2_score = 0
Computers1_score = 0
Computers2_score = 0
def main():
    seed = int(input("Enter an integer to seed the random number generator:  "))
    random.seed(seed)
    for i  in range(10):
        Players1_score = random.randint(1,6)


def players_score_roll_function():
    for i  in range(10):
        Players1_score = random.randint(1,6)
        Players2_score = random.randint(1,6)
        if Players1_score > Players2_score:
            print("player 1 wins.")
            #Players1_score = Players1_score + 1
        elif Players1_score > Players2_score:
            print("player 2 wins")
            #Players2_score = Players2_score + 1
        else:
            print("It's a draw")
    return sum_loop()


def computers_score_roll_functions():
    for i  in range(10):
        Computers1_score = random.randint(1,6)
        if Computers1_score > Computers2_score :
            print("player 1 wins.")
            #computer1_score = Computers1_score + 1
        elif Computers2_score > Computers1_score:
            print("player 2 wins")
            #Computers2_score = Computer2_score + 1
        else:
            print("It's a draw")
            return sum_loop()

def Selection(option1):
    print("Choose one of the following selections \n 1.Reroll your first die \n 2.Reroll your second die \n 3.Keep your original roll")
    option1 = int(input("Enter selection: "))
    if option1 == 1:
        print("oh")
    if option1 == 2:
        print("oh2")
    if option1 == 3:
        return Exit_loop()

def sum_loop(player1_value,player2_value, computer1_value,computer2_value):
    if sum_of_the_dice  == 3:
        score_round =  1000
    if dice == each other:
        score = first_dice*10
    else:
        score = die1 * 10 + die2
    print("You rolled: " + player1_value , random.randint(1,6))
    print("Your score: " + (player1_value + player2_value))

    print("Computer rolled: " + computer1_value , random.randint(1,6))
    print("Computer score:  " + (computer1_value + computer2_value))



def Exit_loop(player1_value,player2_value, computer1_value,computer2_value):
    if sum_of_the_dice  == 3:
        score_round =  1000
    if dice == each other:
        score = first_dice*10
    else:
        score = die1 * 10 + die2

    print("The final scores: ")
    print("You rolled: " + player1_value , random.randint(1,6))
    print("Your score: " + (player1_value + player2_value))

    print("Computer rolled: " + computer1_value , random.randint(1,6))
    print("Computer score:  " + (computer1_value + computer2_value))

    print("Total user score: " + )
    print("Total computer score:  " + )
    return


def Continue_function():
    while True:
        print("Choose one of the following options: \n 1.  Continue Playing \n 2.  Stop Playing ")
        user = int(input("Do you want to keep playing or do you you want to quit?: "))
        if User == 1:
            continue
            players_score_roll_function()
            computers_score_roll_functions()
        if user == 2:
            print("You beat the computer! \nGood job!")
            break





from unittest import mock
from  main import reroll
def test_passed(test_feedback):
    import random
    random.seed(6)
    orginal_inut = mock.builtins.input
    userSelection = "3"
    mock.builtins.input = lambda _: userSelection
    d1, d2, score = reroll(1,2)
    print("die roll ", (1,2), "and score: ", 1000)
    print("User selected: ", userSelection)
    print("New score: ", score)
    return(d1, d2, score) == (1,2,1000)












