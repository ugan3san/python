#!/usr/bin/env python3

from tkinter import *

window = Tk()
window.title("Button class app")


def button_clicked():
    print("Button clicked!")


class Buttons(Button):
    def __init__(self, master, text, command):
        super().__init__(master)
        # Button.__init__(self, master)
        self.master = master
        self["text"] = text
        self["command"] = command
        self["font"] = ("Comic Sans", 30)
        # self['fg']="#7df9ff",
        # self['bg']="#FFFF00",
        # self['activeforeground']="#7df9ff",
        # self['activebackground']="#FFFF00",
        # self['state']=ACTIVE,
        # self['compound']='bottom',


upper_frame = Frame(
    window,
    borderwidth=1,
    highlightbackground="blue",
    highlightthickness=2,
    relief=RAISED,
)
upper_frame.pack(fill="both", side=TOP, expand=1)
upper_frame.rowconfigure(tuple(range(4)), weight=1)
upper_frame.columnconfigure(tuple(range(4)), weight=1)

k = 0
barray = [
    [Buttons(upper_frame, "1", button_clicked) for x in range(4)] for y in range(4)
]
for i in range(len(barray)):
    for j in range(len(barray[i])):
        k += 1
        barray[i][j].grid(row=i, column=j, pady=1, padx=1, sticky="NEWS")
        barray[i][j].config(text=str(k))

window.geometry("400x400+50+10")
window.minsize(400, 400)
window.mainloop()
