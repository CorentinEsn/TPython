import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.scientific_mode = False

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # Affichage
        display = tk.Entry(self.master, textvariable=self.display_var, justify="right", font=('Helvetica', 16), state='readonly')
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Boutons
        self.button_layout = [
            ['7', '8', '9', '/','sin'],
            ['4', '5', '6', '*','cos'],
            ['1', '2', '3', '-','tan'],
            ['0', 'C', 'AC', '+','sqrt'],
            ['=','(',')','^']
        ]

        self.create_buttons()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        mode_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Mode", menu=mode_menu)

        mode_menu.add_command(label="Standard", command=self.set_standard_mode)
        mode_menu.add_command(label="Scientifique", command=self.set_scientific_mode)

    def set_standard_mode(self):
        self.scientific_mode = False
        self.clear_and_create_buttons()

    def set_scientific_mode(self):
        self.scientific_mode = True
        self.clear_and_create_buttons()

    def clear_and_create_buttons(self):
        # Efface les boutons existants
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        # Crée les nouveaux boutons
        for i, row in enumerate(self.button_layout):
            for j, button in enumerate(row):
                if self.scientific_mode or button not in ['sqrt', '^', 'sin', 'cos', 'tan', '(', ')']:
                    tk.Button(self.master, text=button, padx=20, pady=20,
                              command=lambda b=button: self.on_button_click(b)).grid(row=i+1, column=j, sticky="nsew")

    def create_buttons(self):
        self.clear_and_create_buttons()

    def on_button_click(self, button):
        current_display = self.display_var.get()

        if button == '=':
            try:
                result = str(eval(current_display))
                self.display_var.set(result)
            except ZeroDivisionError:
                self.display_var.set("Error: Division by zero")
            except ValueError:
                self.display_var.set("Error: Invalid input")
            except Exception as e:
                self.display_var.set("Error")

        elif button == 'C':
            self.display_var.set(current_display[:-1])

        elif button == 'AC':
            self.display_var.set("")

        elif button == 'sqrt':
            try:
                result = str(math.sqrt(float(current_display)))
                self.display_var.set(result)
            except ValueError:
                self.display_var.set("Error: Invalid input")

        elif self.scientific_mode:
            if button == '^':
                self.display_var.set(current_display + '**')
            elif button in ['sin', 'cos', 'tan']:
                self.display_var.set(button + '(' + current_display + ')')
            else:
                self.display_var.set(current_display + button)
        else:
            self.display_var.set(current_display + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
