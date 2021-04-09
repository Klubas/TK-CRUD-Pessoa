import tkinter as tk
from frontend.lib.text import get_string


class Button(tk.Frame):
    def __init__(self, master, texts, button_text, width=20, command=None, side="left"):
        super().__init__(master)
        button = tk.Button(
            text=get_string(texts, button_text)
            , command=command
            , master=master
            , width=width
        )
        button.pack(side=side, padx=5, pady=5)


class Frame(tk.Frame):
    def __init__(self, master, width=60, padx=0, pady=0):
        super().__init__(master)
        frame = tk.Frame(master, width=width)
        frame.pack(padx=padx, pady=pady)


class Label(tk.Frame):
    def __init__(self, master, label_text, texts=None, width=60):
        super().__init__(master)
        frame = tk.Frame(
            master
            , width=width)

        label = tk.Label(
            text=get_string(texts, label_text)
            , master=frame
            , width=width)
        label.pack(padx=5, pady=7)
        frame.pack()


class LabeledEntry(tk.Frame):
    def __init__(self, master, label_text, texts, width=60, required=False):
        super().__init__(master)

        frame = tk.Frame(master=master)

        text = str(get_string(texts, label_text))
        text = text + "*:" if required else text + ":"

        label = tk.Label(
            text=text
            , master=frame)

        self.entry = tk.Entry(
            master=frame
            , width=width)

        label.pack(anchor="w")

        self.entry.pack(side="right")

        frame.pack()
