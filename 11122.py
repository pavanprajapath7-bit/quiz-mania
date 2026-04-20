from questions import questions
import json
import os

HIGHSCORE_FILE = "highscore.json"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r") as file:
                data = json.load(file)
                return data.get("highscore", 0)
        except:
            return 0
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as file:
        json.dump({"highscore": score}, file)

def run_quiz():
    score = 0
    total = len(questions)

    print("\n🎯 Welcome to the Quiz Game!")
    print("Choose the correct option number (1-4)\n")

    for index, q in enumerate(questions, start=1):
        print(f"Q{index}: {q['question']}")

        for i, option in enumerate(q["options"], start=1):
            print(f"   {i}. {option}")

        try:
            user_choice = int(input("Your answer (1-4): "))

            if user_choice < 1 or user_choice > 4:
                print("❌ Invalid option! No score for this question.\n")
                continue

            selected_answer = q["options"][user_choice - 1]

            if selected_answer == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")

        except ValueError:
            print("❌ Invalid input! Skipping question.\n")

    print("🏁 Quiz Completed!")
    print(f"Your Score: {score}/{total}")

    percentage = (score / total) * 100

    if percentage >= 80:
        print("🔥 Excellent Performance!")
    elif percentage >= 50:
        print("👍 Good Job!")
    else:
        print("💀 Better Luck Next Time!")

    return score

def main():
    highscore = load_highscore()
    print("🏆 Current High Score:", highscore)

    while True:
        score = run_quiz()

        if score > highscore:
            print("🎉 New High Score Achieved!")
            highscore = score
            save_highscore(highscore)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("\nThanks for playing! 🎮")
            break

if __name__ == "__main__":
    main()