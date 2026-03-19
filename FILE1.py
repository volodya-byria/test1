import tkinter as tk
import math


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.geometry("500x730")
        self.root.configure(bg='black')

        self.entry = tk.Entry(self.root, width=40, font=("Arial", 20), justify="right")
        self.entry.pack(pady=15)

        self.create_buttons()

    def click(self, value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + value)

    def clear(self):
        self.entry.delete(0, tk.END)

    def pi(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(math.pi))

    def exponentation(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + "**")

    def sqrt(self):
            result = math.sqrt(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))

    def proc(self):
            result = float(self.entry.get()) / 100
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))

    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def calculate(self):
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)

    def create_buttons(self):
        buttons = [
            ['%', '(', ')', 'C'],
            ['π', '^', '√', '←'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '/'],
            ['0', '.', '=', '*'],
        ]

        for row in buttons:
            frame = tk.Frame(self.root, bg='black')
            frame.pack()
            for btn_text in row:
                if btn_text == '=':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.calculate)
                elif btn_text == 'C':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.clear)
                elif btn_text == 'π':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.pi)
                elif btn_text == '←':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.backspace)
                elif btn_text == '√':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.sqrt)
                elif btn_text == '%':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.proc)
                elif btn_text == '^':
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=self.exponentation)
                else:
                    btn = tk.Button(frame, text=btn_text, width=12, height=5,command=lambda x=btn_text: self.click(x))

                btn.pack(side='left', padx=2, pady=3)
                btn.configure(bg='#ffba52', fg='black', font=12)


    def run(self):
        self.root.mainloop()


# Создание и запуск калькулятора
if __name__ == "__main__":
    calc = Calculator()
    calc.run()