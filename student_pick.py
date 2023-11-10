import tkinter as tk
from tkinter import *
import pandas as pd
import random
from pandas import DataFrame


class StudentPicker:
    def __init__(self, master):
        self.master = master
        master.title("Random student picker")
        master.geometry("700x450+200+200")
        master['background'] = '#856ff8'

        self.topLabel = Label(master, text="Random student picker", font=("Ink Free", 40, "bold"),bg ="#856ff8", fg='white')
        self.topLabel.pack(pady=20)

        df = pd.read_csv('students.txt', encoding='utf-8')
        df.columns = ["name"]
        self.students = df['name'].tolist()
        self.temp = []

        self.pickButton = Button(root, text="Pick our winner! ;)", font=("Comic Sans MS", 18), command=lambda: self.pick())
        self.pickButton.pack(pady=20)
        self.absentButton = Button(master, text="Student is absent :(", font=("Comic Sans MS", 10),
                                   command=lambda: self.check())
        self.absentButton.pack(pady=10)

        self.winnerLabel = Label(master, text='Next student:', font=("Comic Sans MS", 20),bg="#856ff8")
        self.winnerLabel.pack(pady=20)

        self.left = Label(master, pady=10, bg='#856ff8')
        self.left.pack()

        self.writeButton = Button(master, text="Print", font=("Comic Sans MS", 10),
                                   command=lambda: self.write())
        self.writeButton.pack(pady=5,side=RIGHT)

    def pick(self):
        if len(self.temp) == 0:
            self.temp = self.students.copy()
        self.student = random.choice(self.temp)
        self.winnerLabel.config(text="" + self.student, font=("Comic Sans MS", 20))
        self.temp.remove(self.student)

        self.left.config(text="Students left : " + str(len(self.temp)), font=("Comic Sans MS", 16),bg='#856ff8')

    def check(self):
        self.temp.append(self.student)
        self.winnerLabel.config(text="" + self.student, font=("Comic Sans MS", 20))
        self.left.config(text="Students left : " + str(len(self.temp)), font=("Comic Sans MS", 16),bg='#856ff8')

    def write(self):
        with open('students.txt', 'w') as f:
            for item in self.temp:
                f.write("%s\n" % item)


root = Tk()
my_gui = StudentPicker(root)
root.mainloop()
