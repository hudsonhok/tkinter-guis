# https://www.youtube.com/watch?v=ibf5cx221hk

import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text='Notes', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0) # Disable tearoff from gui
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_command(label="Close without question", command=exit)
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Show message', command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.textbox = tk.Text(self.root, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        # Need a variable for the check button for storing value T/F
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='Show messagebox', font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show message', font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text='Clear', font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    def show_message(self):
        #print('Hello world')
        #print(self.check_state.get()) # Gets state of the checkbox
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END)) # .get(index, to_what_position)
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        #print(event) # pay attention to state and keysym
        #print(event.keysym)
        #print(event.state)
        if event.state == 4 and event.keysym == 'Return':
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.root.destroy() # Closes the window

    def clear(self):
        self.textbox.delete('1.0', tk.END)
MyGUI()