questions = {
    "who created pyhton ? : " : "A",
    "what year was the python created ? : " : "B",
    "python is tributed to which comedy group ? : " : "C",
    "is the earth round ? : ": "D"
}

options= [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

#---------------------------------------------------------------------------------------------------#
def new_game():
    user_guess = []
    question_number = 1 
    count= 0

    for key in questions:
        print("----------------------------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        question_number+= 1
        guess = input("choose from (A , B , C , D ): ")
        guess = guess.upper()
        right_anwser = questions[key] 
        user_guess.append(guess)
        count += check_answer(right_anwser,guess,count)
    total_score(str(count),user_guess)
    playagain()

#---------------------------------------------------------------------------------------------------#

def check_answer(correct,user,count):
    if correct == user : 
        print("----------------------------------------------------")
        print("     CORRECT     ")
        return 1

    else:
        print("----------------------------------------------------")
        print ("    WRONG   ")
        return 0
    

def total_score(a, userguess):
    print("----------------------------------------------------")
    print("RESULT")
    print("----------------------------------------------------")
    print(" your answer  - ", end =" ")
    for i in userguess:
        print( end=" " + i )
    print(" \ncorrect answers", end =" ")
    for i in questions:
        print( end=" "+ questions[i] )
    print (" \nyour total score is : " + str(a) + "/" + str(len(questions)))

def playagain():
    user_i = input("do you want to play again?  ( y/n ) : " ).lower()
    if user_i == "y":
        new_game()
    else:
        print("thanks for playing ")
        pass   

new_game()