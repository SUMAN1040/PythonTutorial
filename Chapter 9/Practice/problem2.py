import random
# The game() function in program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() functions breaks the Hi-score


def game():
    print("You are playing the game")
    score = random.randint(1, 62)
    #Fetch the high score
    with open("Hi-score.txt") as f:
        Hi_score = f.read()
        if(Hi_score!=""):
            Hi_score = int(Hi_score)
        else:
            Hi_score=0
    print(f"Your score is {score}")
    if(score>Hi_score):
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))



    return score

game()