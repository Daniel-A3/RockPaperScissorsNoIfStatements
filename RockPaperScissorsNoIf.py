# Python Rock Paper Scissors without if statements
# Using matrix's
import random, sys, time, os

def quit():
    sys.exit()

while True:
    userChoice = input("Please enter your choice"
                       "('rock', 'paper', or 'scissors') "
                       "or 'q' to quit = ").lower()
    print("-\nYou chose " + userChoice)

    choicesDict = { "rock" : 0, "paper" : 1, "scissors" : 2, "q" : quit }
    # Sees if the user pressed 'q' to quit
    try:
        choicesDict[userChoice]()
    except (KeyError, TypeError):
        # Assigns a number to each of the choices, if it's an invalid choice it returns 3
        userChoiceIndex = choicesDict.get(userChoice, 3)

    choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices)
    computerChoiceIndex = choicesDict.get(computerChoice)
    print("-\nComputer Chose %s" % computerChoice)
    # All of the possible win, lose, draw or invalid combinations
    resultMatrix = [[0, 2, 1],
                     [1, 0, 2],
                     [2, 1, 0],
                     [3, 3, 3]]
    # Founds out which combination is the result
    resultIndex = resultMatrix[userChoiceIndex][computerChoiceIndex]

    resultMessage = ["It's a tie!", "You Win!", "You lost!",
                     "You didn't choose 'rock', 'paper', or 'scissors'."]
    result = resultMessage[resultIndex]
    print("-\n" + result)
    time.sleep(3)
    os.system("clear") # This only works if you running the program on your terminal and it's unix based.
    # If you want this to work on windows just replace 'clear' with 'cls'