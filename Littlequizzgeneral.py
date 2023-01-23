#
#
# Little quizz
#
#
#Alexis.D 
#2023


#Import library
from random import shuffle

# Quiz questions 
# Define the questions and her answers

def questions() :
    questions = {
        "Who is in 2023 the French President ?"
        "Who is the US president in 2023 ?"
        "What is the capital of France ?"
        "What is the capital of the US ?"
        "What is the capital of the UK ?"
        "Who write the song 'Hybrid Theory' ?"
        "Who is the singer of the song 'Numb' ?"
        "Who is nothing nowere ?"
        "What is the biggest country of the world ?"
    }

def answer() :
    answer = {
        "Emmanuel Macron" : "Who is in 2023 the French President ?",
        "Joe Biden" : "Who is the US president in 2023 ?",
        "Paris" : "What is the capital of France ?",
        "Washington" : "What is the capital of the US ?",
        "London" : "What is the capital of the UK ?",
        "Linkin Park" : "Who write the song 'Hybrid Theory' ?",
        "Chester Bennington" : "Who is the singer of the song 'Numb' ?",
        "Nothing" : "Who is nothing nowere ?",
        "Russia" :  "What is the biggest country of the world ?"
    }
#Launch the quiz by starting a dialog with the user
def start_quiz() :
    print("Welcome to the quiz !")
    print("You will have to answer 6 questions.")
    print("Let's start !")

    for questions, answer in questions.items() : #Should be questions.items() but it doesn't work
        print(questions)
        user_answer = input("Answer : ")
        if user_answer == answer :
            print("Correct !")
        else :
            print("Wrong !")
            print("The correct answer is : " + answer)

# Nothing to see here









# Really, nothing to see here










# I'm not even kidding














# I'm serious


















# I'm not kidding













# What do you think ?














# Finding a secret ?










# Finding a task list of the futur of the  quiz ??













# ha ha ha ha ha ha





























# To be created/done
# See why this shit isn't working
# Fix it
# Make it work
# Add a score system
# Add more questions