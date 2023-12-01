import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.col = 3
        self.row = 0
        self.create_widgets()

    def create_widgets(self):
        # Affichage
        display = tk.Entry(self.master, textvariable=self.display_var, justify="right", font=('Helvetica', 16))
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")



        # Boutons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '', '0', '=', '+',
            '', '','AC' ,'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '':
                tk.Button(self.master, state="disabled", padx=20, pady=20).grid(row=row_val, column=col_val, sticky="nsew")
            else:
                tk.Button(self.master, text=button, padx=20, pady=20, command=lambda b=button: self.on_button_click(b)).grid(
                    row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > self.col:
                col_val = 0
                row_val += 1
        self.row = row_val



    def on_button_click(self, button):
        current_display = self.display_var.get()

        if button == '=':
            try:
                result = str(eval(current_display))
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Error")

        elif button == 'C':
            self.display_var.set(current_display[:-1])

        elif button == 'AC':
            self.display_var.set("")

        else:
            self.display_var.set(current_display + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    for i in range(app.row):
        root.rowconfigure(i, weight=1)
    for i in range(app.col+1):
        root.columnconfigure(i, weight=1)
    root.mainloop()