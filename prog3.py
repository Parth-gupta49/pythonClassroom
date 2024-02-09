import tkinter as tk
import re

def test_regex():
    user_input = entry_string.get()
    regex_pattern = entry_regex.get()

    if re.match(regex_pattern, user_input):
        result_label.config(text="Match!")
    else:
        result_label.config(text="No match.")

root = tk.Tk()
root.title("String Pattern Matching")

label_string = tk.Label(root, text="Enter String:")
label_string.grid(row=0, column=0)

entry_string = tk.Entry(root, width=30)
entry_string.grid(row=0, column=1)

label_regex = tk.Label(root, text="Enter Regular Expression:")
label_regex.grid(row=1, column=0)

entry_regex = tk.Entry(root, width=30)
entry_regex.grid(row=1, column=1)

test_button = tk.Button(root, text="Test Pattern", command=test_regex)
test_button.grid(row=2, column=0, columnspan=20)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=20)

root.mainloop()