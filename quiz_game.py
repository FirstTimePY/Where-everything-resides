#-------------------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your guess (A, B or C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


#-------------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correct! +1 Point!")
        return 1
    else:
        print("Wrong! No points.")
        return 0
    
#-------------------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------------")
    print("Results")
    print("-------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score)+"%")

#-------------------------------------
def play_again():
    
    response = input("Do you want to play again? (y/n): ")
    response = response.lower()

    if response == "y":
        return True
    else:
        return False

#-------------------------------------


questions = {
    "Who farted on July 7th 1941?: ": "A",
    "What year did Japan get boom boom?: ": "B",
    "googoo gaga?: ": "C",
    "Is C garbage?: ": "C"
}


options = [["A. Jeff Bezos", "B. Elon Musk", "C. Ronnie Mcnutt"],
           ["A. 1969", "B. 1945", "C. 238 BC"],
           ["A. No", "B. Maybe", "C. Duh"],
           ["A. I love C!", "B. No its good", "C. Ew its obviously garbage"]]

new_game()

while play_again():
    new_game()

print("\nCya!")  




