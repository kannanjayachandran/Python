import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from nltk.corpus import words


"""
# Uncomment the following lines to download the words corpus
nltk.download("words")
"""


class Checker_main:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.letter = ScrolledText(self.root, font=("Helvetica", 16))
        self.letter.bind("<KeyRelease>", self.check)
        self.letter.pack()

        self.previous_spaces = 0

        self.root.mainloop()

    def check(self, event):

        content = self.letter.get("1.0", tk.END)
        space_count = content.count(" ")

        for part in self.letter.tag_names():
            self.letter.tag_delete(part)

        if space_count != self.previous_spaces:
            self.previous_spaces = space_count

            for word in content.split(" "):

                if re.sub(r"[^\w]", '', word.lower()) not in words.words():
                    position = content.find(word)
                    self.letter.tag_add(
                        word, f"1.{position}", f"1.{position + len(word)}")
                    self.letter.tag_config(word, foreground="red")


Checker_main()
