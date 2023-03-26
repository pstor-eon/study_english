import pandas as pd
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, StringVar, LEFT

def import_data(filename):
    return pd.read_excel(filename, engine='openpyxl')

class StudyKorean:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.index = -1
        self.correct_answers = 0
        self.total_words = len(self.data)

        self.master.title("Learn English Words")
        self.master.geometry("430x230")

        self.word_label = Label(self.master, text="Korean:", font=("Arial", 14))
        self.word_label.pack(pady=10)

        self.hint_label = Label(self.master, text="Hint: ", font=("Arial", 12))
        self.hint_label.pack(pady=5)

        self.entry = Entry(self.master, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.focus_set()
        self.entry.bind('<Return>', self.check_word)

        self.button_frame = Frame(self.master)
        self.button_frame.pack(pady=5)

        self.check_button = Button(self.button_frame, text="Check", font=("Arial", 12), command=self.check_word)
        self.check_button.pack(side=LEFT, padx=5)

        self.hint_button = Button(self.button_frame, text="Show hint", font=("Arial", 12), command=self.show_hint)
        self.hint_button.pack(side=LEFT, padx=5)

        self.skip_button = Button(self.button_frame, text="Skip", font=("Arial", 12), command=self.next_word)
        self.skip_button.pack(side=LEFT, padx=5)

        self.stop_button = Button(self.button_frame, text="Stop", font=("Arial", 12), command=self.end_game)
        self.stop_button.pack(side=LEFT, padx=5)


        self.progress_text = StringVar()
        self.progress_label = Label(self.master, textvariable=self.progress_text, font=("Arial", 12))
        self.progress_label.pack(pady=5)
        self.update_progress()

        self.next_word()

    def next_word(self):
        if self.correct_answers == self.total_words:
            self.end_game()
            return

        self.data = self.data.sample(frac=1).reset_index(drop=True)
        self.index += 1
        if self.index >= len(self.data):
            self.index = 0

        self.current_word = self.data.iloc[self.index]
        self.word_label.config(text="Korean: " + self.current_word['korean'])
        self.hint_label.config(text="Hint: ")
        self.entry.delete(0, "end")

    def check_word(self, event=None):
        user_input = self.entry.get().strip()
        if user_input.lower() == self.current_word['english'].lower():
            self.correct_answers += 1
            self.update_progress()
            self.data.drop(self.index, inplace=True)
            self.data.reset_index(drop=True, inplace=True)
            self.next_word()
        else:
            messagebox.showerror("Incorrect", "The answer is incorrect.")
            self.show_hint()
            self.next_word()

    def show_hint(self):
        self.hint_label.config(text="Hint: " + self.current_word['hint'])

    def update_progress(self):
        self.progress_text.set(f"Progress: {self.correct_answers}/{self.total_words}")

    def end_game(self):
        messagebox.showinfo("Game over", f"You've guessed {self.correct_answers}/{self.total_words} words correctly.")
        self.master.destroy()

if __name__ == "__main__":
    data = import_data("words.xlsx")
    data = data.sample(frac=1).reset_index(drop=True)

    root = Tk()
    app = StudyKorean(root, data)
    root.mainloop()
