import csv
import random
from tkinter import *

def load_words_from_csv(file_name):
    words = []

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            korean, english = row
            words.append((korean, english))

    return words

def create_problem(remaining_words):
    correct_word = random.choice(remaining_words)
    wrong_words = random.sample([word for word in words if word != correct_word], 4)
    options = wrong_words + [correct_word]
    random.shuffle(options)

    return correct_word, options

def check_answer(user_choice, correct_word, lbl_result):
    global remaining_words, correct_count

    if user_choice == correct_word[1]:
        lbl_result.config(text="정답입니다!", fg="green")
        remaining_words.remove(correct_word)
        correct_count += 1
        start_game()
    else:
        lbl_result.config(text=f"틀렸습니다. 정답은 {correct_word[1]} 입니다.", fg="red")
        app.after(2000, start_game)

    lbl_score.config(text=f"{correct_count}/{len(words)}")

    if not remaining_words:
        lbl_result.config(text="모든 문제를 맞추셨습니다! 프로그램을 종료합니다.", fg="blue")
        app.after(3000, close_app)

def start_game():
    correct_word, options = create_problem(remaining_words)
    lbl_korean.config(text=correct_word[0])
    lbl_result.config(text="")
    for i, option in enumerate(options):
        btn_options[i].config(text=option[1], command=lambda choice=option[1]: check_answer(choice, correct_word, lbl_result))

def close_app():
    app.destroy()

if __name__ == "__main__":
    words = load_words_from_csv("words.csv")
    remaining_words = words.copy()
    correct_count = 0

    app = Tk()
    app.title("영어 단어 공부")

    lbl_score = Label(app, font=("Helvetica", 20), text=f"{correct_count}/{len(words)}")
    lbl_score.pack(pady=10)

    lbl_korean = Label(app, font=("Helvetica", 30))
    lbl_korean.pack(pady=20)

    btn_options = []
    for _ in range(5):
        btn = Button(app, font=("Helvetica", 15), width=20, height=2)
        btn.pack(pady=5)
        btn_options.append(btn)

    lbl_result = Label(app, font=("Helvetica", 20))
    lbl_result.pack(pady=20)

    start_game()

    btn_exit = Button(app, text="종료", font=("Helvetica", 15), width=20, height=2, command=close_app)
    btn_exit.pack(pady=20)

    app.mainloop()
