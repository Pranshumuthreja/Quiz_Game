import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from PIL import Image, ImageTk
import pygame

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        self.questions = self.load_questions("quiz_data.xlsx")
        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        # Initialize pygame mixer for sound effects
        pygame.mixer.init()

        # Load sound files
        self.correct_sound = pygame.mixer.Sound("correct.wav.mp3")
        self.wrong_sound = pygame.mixer.Sound("wrong.wav.mp3")

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Question Label
        self.question_label = tk.Label(self.main_frame, text="", wraplength=500, justify="center", font=("Arial", 14))
        self.question_label.pack(pady=10)

        # Options Frame
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.selected_option, value="", anchor="w", font=("Arial", 12))
            btn.pack(anchor="w", pady=5)
            self.option_buttons.append(btn)

        # Feedback Label
        self.feedback_label = tk.Label(self.main_frame, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(self.main_frame, length=200, mode='determinate')
        self.progress.pack(pady=10)

        # Next Button
        self.next_button = tk.Button(self.main_frame, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

    def load_questions(self, file_path):
        df = pd.read_excel(file_path)
        questions = []
        for index, row in df.iterrows():
            question = {
                "question": row["Question"],
                "options": [row["Option1"], row["Option2"], row["Option3"], row["Option4"]],
                "answer": row["Answer"]
            }
            questions.append(question)
        return questions

    def fade_in(self, widget, text, delay=50):
        widget.config(text="")
        for i in range(len(text) + 1):
            widget.after(i * delay, lambda i=i: widget.config(text=text[:i]))

    def load_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.fade_in(self.question_label, q["question"])
            self.selected_option.set(None)
            for i, option in enumerate(q["options"]):
                self.fade_in(self.option_buttons[i], option)
                self.option_buttons[i].config(value=option)
            self.feedback_label.config(text="")
            self.update_progress()
        else:
            self.end_quiz()

    def next_question(self):
        selected_answer = self.selected_option.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer before proceeding.")
            return

        correct_answer = self.questions[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
            self.animate_feedback("Correct!", "green")
            self.correct_sound.play()
        else:
            self.animate_feedback(f"Wrong. The correct answer is {correct_answer}.", "red")
            self.wrong_sound.play()

        self.current_question += 1
        self.root.after(3000, self.load_question)

    def animate_feedback(self, text, color):
        self.feedback_label.config(text=text, fg=color)
        for i in range(0, 256, 10):
            self.feedback_label.after(i * 2, lambda i=i: self.feedback_label.config(fg=f"#{i:02x}{i:02x}{i:02x}"))

    def update_progress(self):
        progress = (self.current_question / len(self.questions)) * 100
        self.animate_progress_bar(progress)

    def animate_progress_bar(self, target_value):
        current_value = self.progress['value']
        step = (target_value - current_value) / 10
        for i in range(11):
            self.root.after(i * 50, lambda i=i: self.progress.step(step))

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
