# Little quizz

# Simple quiz en utilisant les dictionnaires
def questions() :
    questions = {
        "Who is in 2023 the French President ?" : "Emmanuel Macron",
        "Who is the US president in 2023 ?" : "Joe Biden",
        "What is the capital of France ?" : "Paris",
        "What is the capital of the US ?" : "Washington",
        "What is the capital of the UK ?" : "London",
        "Who write the song 'Hybrid Theory' ?" : "Linkin Park",
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
# There's nothing to see here
# I'm serious
# There's nothing to see here
# I'm not kidding

# To be created/done
# See why this shit isn't working
# Fix it
# Make it work
# Add a score system
# Add more questions