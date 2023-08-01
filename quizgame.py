quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

def play_quiz():
    score = 0
    
    # Present Quiz Questions
    for question, answer in quiz_questions.items():
        print(question)
        user_answer = input("Your answer: ")
        
        # Evaluate the User's Answer
        if user_answer.lower() == answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print("The correct answer is:", answer)
        
        print() # Add a newline for spacing
        
    # Display Final Results
    print("Quiz Complete!")
    print("Your score is:", score)
    
    # Play Again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        play_quiz()
    else:
        print("Goodbye!")

# Display Welcome Message and Rules
print("Welcome to the Quiz Game!")
print("You will be asked multiple-choice or fill-in-the-blank questions.")
print("Let's start!")

# Start the quiz game
play_quiz()
