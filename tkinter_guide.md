# Tkinter Guide

## Introduction

Tkinter is the standard GUI library for Python, which allows us to create windows, dialogs, buttons, menus, and other widgets in our applications.

## Basic Concepts

1. **Widgets**: The building blocks of a GUI application, such as buttons, labels, text boxes, and frames.
2. **Root Window**: The main window of a Tkinter application, created by instantiating the `Tk` class.
3. **Event Loop**: Tkinter applications run an event loop, which waits for events (like button clicks or key presses) and dispatches them to appropriate handlers. The event loop is started with the `mainloop` method.

## Basic Example

Here's a basic example of a simple Tkinter application:

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Hello Tkinter")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)  # Add the label to the window

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)  # Add the button to the window

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()

# Run the application
root.mainloop()
```
##  Some Widgets
### Label


For more resources you can check out the following documentations:
* https://docs.python.org/3/library/tk.html
* https://www.tutorialspoint.com/python/python_gui_programming.htm
* For larger apps you can use classes: https://www.youtube.com/watch?v=eaxPK9VIkFM