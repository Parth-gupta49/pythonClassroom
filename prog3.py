import tkinter as tk
import re

def test_regex():
    user_input = inputForString.get()
    regex_pattern = inputForRegex.get()

    if re.search(regex_pattern, user_input):
        labelForResult.config(text="Match!")
    else:
        labelForResult.config(text="No match.")

rootWindow = tk.Tk()
rootWindow.geometry("300x150")
rootWindow.title("String Pattern Matching")

labelForString = tk.Label(rootWindow, text="Enter String:")

inputForString = tk.Entry(rootWindow, width=20)

labelForRegex = tk.Label(rootWindow, text="Enter Regular Expression:")

inputForRegex = tk.Entry(rootWindow, width=20)

button = tk.Button(rootWindow, text="Test Pattern", command=test_regex)

labelForResult = tk.Label(rootWindow, text="")

labelForString.pack()  
inputForString.pack()
labelForRegex.pack()
inputForRegex.pack()
button.pack()
labelForResult.pack()
rootWindow.mainloop()