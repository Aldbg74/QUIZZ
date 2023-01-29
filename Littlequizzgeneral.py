#
#
# Little quizz
#
#
#Alexis.D 
#2023

#-----------------
def new_game():

    guesses =[]
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("--------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)
            
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
        
        
    display_score(correct_guesses, guess)
    
#-----------------
def check_answer(answer, guess):
    
    if answer == guess:
        print(" CORRECT ! ")
        return 1
    else:
        print("WRONG")
        return 0
    
    
#-----------------
def display_score(correct_guesses, guesses):
    print("--------------------")
    print(" RESULTS ")
    print("--------------------")
    
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end="")
    print()
    
    print("guesses: ", end = "")
    for i in guesses:
        print(i, end="")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("You have a score of :"+str(score)+"%")
    
#-----------------
def play_again():
    reponse = input("Do you want to play or play again ? (y or n) :")
    
    if reponse == "y":
        return True
    else:
        return False
        
#-----------------

questions = {
 "Who is the US President in 2022" : "B",
 "Who is Linkin Park" : "B",
 "What year was Apple created ?" : "A"
 }

options = [["A. Donald Trump", "B. Joe Biden", "C. Elon Musk"],
["A. A politician", "B. A music band", "C. A gamer"],
["A. 1976", "B. 1978", "C.1975"]]

new_game

while play_again():
    new_game()
    
print ("Bye")
