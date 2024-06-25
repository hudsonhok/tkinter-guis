import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("My first gui")
root.geometry("800x500")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)  # Add the label to the window

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)  # Add the button to the window

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1) # We want the button to stretch
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
# Grid takes row and column
# Sticky is for where you want it to stretch
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=350, y=300, height=50, width=100)

# Run the application
root.mainloop()