# Display a welcome message to the user

def display_welcome_message():
    print("Welcome to the Ultimate Quiz Mania!!")
    print("Put your skills to the test and discover your score!!\n")

# Display questions.

def get_questions():
    return [
{"question": "Which is the largest continent by land area?",
        "options": ["A. Africa", "B. Asia", "C. Europe", "D. Antarctica"],
        "answer": "B"},

{"question": "What is the main gas found in the Earth's atmosphere?",
            "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
            "answer": "C"},

{"question": "Which planet has the most moons?",
            "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
            "answer": "C"},

{"question": "Which part of the cell is responsible for generating energy?",
            "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Endoplasmic reticulum"],
            "answer": "C"},

{"question": "Who was the first President of the United States?",
            "options": ["A. Thomas Jefferson", "B. Abraham Lincoln", "C. George Washington", "D. John Adams"],
            "answer": "C"},

{"question": "What is the largest internal organ in the human body?",
            "options": ["A. Lungs", "B. Heart", "C. Kidneys", "D. Liver"],
            "answer": "D"},

{"question": "What is the percentage of the Earth covered by water?",
            "options": ["A. 51%", "B. 61%", "C. 71%", "D. 81%"],
            "answer": "C"},

{"question": "Which of the following is not a Japanese dish?",
            "options": ["A. Sushi", "B. Ramen", "C. Babi guling", "D. Udon"],
            "answer": "C"},

{"question": "Which member of the Spice Girls was known as 'Sporty Spice'?",
            "options": ["A. Melanie Chisholm", "B. Emma Bunton", "C. Geri Halliwell", "D. Victoria Adams"],
            "answer": "A"},

{"question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Jupiter", "C. Saturn", "D. Mars"],
            "answer": "D"}
    ]

#User Input and calculate score
def ask_questions(questions):
    score = 0

# The enumerate function iterates through the list questions, returning both the index (idx, starting at 1) and the question dictionary (q). 
# This loop ensures each question in the list is presented to the user.
    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}: {q['question']}")
        for option in q["options"]:
            print(option)
        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please select A, B, C, or D.")
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    return score

def display_results(score, total):
    print(f"Your total score: {score}/{total}")
    if score == total:
        print("Excellent! You got all answers correct!")
    elif score > total // 5:
        print("Great job! You scored above average!")
    else:
        print("Better luck next time. Keep practicing!")

def display_thank_you_message():
    print("\nThank you for taking the quiz! Hope you enjoyed it!")

def main():
    display_welcome_message()
    questions = get_questions()
    score = ask_questions(questions)
    display_results(score, len(questions))
    display_thank_you_message()

if __name__ == "__main__":
    main() 


