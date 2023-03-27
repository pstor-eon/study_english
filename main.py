import os
import random
import subprocess
from tkinter import *

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("English Learning App")
        self.master.geometry("450x150")

        self.title = Label(self.master, text="Choose an option:", font=("Arial", 14))
        self.title.pack(pady=10)

        self.button_frame_top = Frame(self.master)
        self.button_frame_top.pack(pady=5)

        self.study_button = Button(self.button_frame_top, text="1. 영어 단어 맞추기", font=("Arial", 12), command=self.start_study_korean, width=20)
        self.study_button.pack(side=LEFT, padx=5)

        self.flashcards_button = Button(self.button_frame_top, text="2. 영어 카드 맞추기", font=("Arial", 12), command=self.start_flashcards, width=20)
        self.flashcards_button.pack(side=LEFT, padx=5)

        self.button_frame_bottom = Frame(self.master)
        self.button_frame_bottom.pack(pady=5)

        self.random_button = Button(self.button_frame_bottom, text="3. 랜덤 실행", font=("Arial", 12), command=self.start_random, width=20)
        self.random_button.pack(side=LEFT, padx=5)

        self.exit_button = Button(self.button_frame_bottom, text="종료", font=("Arial", 12), command=self.master.quit, width=20)
        self.exit_button.pack(side=LEFT, padx=5)

    def start_study_korean(self):
        subprocess.Popen(["python", "study_english.py"])

    def start_flashcards(self):
        subprocess.Popen(["python", "english_card_game.py"])

    def start_random(self):
        random_choice = random.choice([self.start_study_korean, self.start_flashcards])
        random_choice()

if __name__ == "__main__":
    main_root = Tk()
    main_app = MainMenu(main_root)
    main_root.mainloop()
