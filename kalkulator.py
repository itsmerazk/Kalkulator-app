import tkinter as tk
from tkinter import messagebox
import math

class KalkulatorSains:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sains")

       
        bg_color = "#f0f0f0"
        btn_color = "#d9d9d9"
        font_color = "#333333"

        
        self.entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        
        basic_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        
        for (text, row, column) in basic_buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), bg=btn_color, fg=font_color, 
                               command=lambda t=text: self.on_basic_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

           
            if text in ('=', 'C'):
                button.config(bg="#ff6600", fg="white")

        
        menu_button = tk.Menubutton(root, text="Menu", font=('Arial', 14), bg=btn_color, fg=font_color)
        menu_button.grid(row=1, column=4, columnspan=2, padx=5, pady=5)
        menu_button.menu = tk.Menu(menu_button, tearoff=0, font=('Arial', 14))
        menu_button["menu"] = menu_button.menu
        menu_button.menu.add_command(label="sin", command=lambda: self.on_special_button_click('sin'))
        menu_button.menu.add_command(label="cos", command=lambda: self.on_special_button_click('cos'))
        menu_button.menu.add_command(label="tan", command=lambda: self.on_special_button_click('tan'))
        menu_button.menu.add_command(label="log", command=lambda: self.on_special_button_click('log'))
        menu_button.menu.add_command(label="sqrt", command=lambda: self.on_special_button_click('sqrt'))

    def on_basic_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

    def on_special_button_click(self, text):
        if text == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'log':
            try:
                result = math.log10(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    kalkulator = KalkulatorSains(root)
    root.mainloop()
