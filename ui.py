THEME_COLOR = "#375362"
from tkinter import *

class QuizzInterface:

    def __init__(self):
        self.window= Tk()
        self.window.title("Trivia")
        self.window.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg= THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas= Canvas(width= 300, height=250, bg="white")
        self.canvas.grid(column= 0, row =1, columnspan= 2, pady=50)
        self.question_text = self.canvas.create_text(150,125,text="text comes here", font=("Arial", 20, "italic"))

        false_img = PhotoImage(file="images/false.png")
        self.false_button= Button(image=false_img, highlightthickness= 0)
        self.false_button.grid(column= 1, row =2)
        true_img= PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness= 0)
        self.true_button.grid(column=0, row=2)


        self.window.mainloop()
