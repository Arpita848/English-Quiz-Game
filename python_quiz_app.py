#final
import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    {
        "question": "What is the capital letter of the alphabet after A?",
        "options": ["B", "C", "D", "E"],
        "answer": "B",
    },
    {
        "question": "Which word is a noun?",
        "options": ["Run", "Beautiful", "Table", "Quickly"],
        "answer": "Table",
    },
    {
        "question": "What is the opposite of 'big'?",
        "options": ["Small", "Tall", "Wide", "Bright"],
        "answer": "Small",
    },
    {
        "question": "Which one is a fruit?",
        "options": ["Apple", "Car", "Table", "Shoe"],
        "answer": "Apple",
    },
    {
        "question": "How many legs does a dog have?",
        "options": ["2", "3", "4", "5"],
        "answer": "4",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English Quiz for Kids")

        self.current_question = 0
        self.score = 0

        # Question label
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        # Options buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=20, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Next question button
        self.next_button = tk.Button(root, text="Next Question", font=("Arial", 14), command=self.next_question)
        self.next_button.pack(pady=20)

        # Start quiz
        self.load_question()

    def load_question(self):
        """Load the current question and options."""
        question_data = questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question_data['question']}")
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, state=tk.NORMAL)

    def check_answer(self, idx):
        """Check if the selected answer is correct."""
        selected_option = self.option_buttons[idx].cget("text")
        correct_answer = questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done! That's the correct answer.")
        else:
            messagebox.showerror("Wrong!", f"Oops! The correct answer was '{correct_answer}'.")
        
        # Disable options after an answer
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)

    def next_question(self):
        """Load the next question or show the final score."""
        self.current_question += 1
        if self.current_question < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(questions)}")
            self.root.destroy()  # Close the app

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()