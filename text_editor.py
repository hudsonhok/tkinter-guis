import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",  # Sets the default file extension
        filetypes=[("Text Documents", "*.txt")]  # Filters for .txt file types only
    )
    if file_path:
        if file_path.endswith(".txt"):
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
        else:
            messagebox.showerror("Invalid file", "Only .txt files can be opened.")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",  # Sets the default file extension
        filetypes=[("Text Documents", "*.txt")]  # Filters for .txt file types only
    )
    if file_path:
        if not file_path.endswith(".txt"):
            file_path += ".txt"
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def exit_editor():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# Set up the main application window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Create the text area
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both') # expand uses any extra space in parent window, fill fills the space of the widget

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Run the application
root.mainloop()
