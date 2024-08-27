def ask_question(question, options, correct_answer):
    """
    This function prints a question, options, and checks if the user's answer is correct.
    
    Parameters:
    - question: The question to be asked.
    - options: A list of possible answers.
    - correct_answer: The correct option for the answer.
    
    Returns:
    - True if the answer is correct, otherwise False.
    """
    print(question)
    for index, option in enumerate(options):
        print(f"{chr(65 + index)}. {option}")
    
    while True:
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        print("Invalid input. Please choose A, B, C, or D.")
    
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.")
        return False

def quiz_game():
    """
    This function runs the entire quiz game.
    """
    questions = [
        {
            "question": "What is the capital of Greece?",
            "options": ["Berlin", "Madrid", "Athens", "Rome"],
            "correct": "C"
        },
        {
            "question": "What is 2 ** 4?",
            "options": ["8", "16", "12", "6"],
            "correct": "B"
        },
        {
            "question": "Which planet is known as the Morning and Evening Star?",
            "options": ["Earth", "Venus", "Jupiter", "Saturn"],
            "correct": "B"
        },
        {
            "question": "Who wrote 'Atomic Habits'?",
            "options": ["James Clear", "Mark Twain", "Ernest Hemingway", "J.K. Rowling"],
            "correct": "A"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["0", "1", "2", "3"],
            "correct": "C"
        }
    ]

    print("Welcome to the Python Quiz Game!")
    print("You will be asked 5 multiple-choice questions. Choose the correct option by entering A, B, C, or D.\n")

    score = 0
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct"]):
            score += 1

    print(f"\nQuiz Over! Your total score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz_game()
