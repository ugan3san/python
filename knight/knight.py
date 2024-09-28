#!/usr/bin/env python3

from tkinter import *

window = Tk()
window.title("Button class app")


def button_clicked(x, y):
    print("Button clicked!")
    print(x, y)


class Buttons(Button):
    def __init__(self, master, text, command):
        super().__init__(master)
        # Button.__init__(self, master)
        self.master = master
        self["text"] = text
        self["command"] = lambda: command(self.x, self.y)
        self["font"] = ("Comic Sans", 30)
        # self['fg']="#7df9ff",
        # self['bg']="#FFFF00",
        # self['activeforeground']="#7df9ff",
        # self['activebackground']="#FFFF00",
        # self['state']=ACTIVE,
        # self['compound']='bottom',
        self.x = 0
        self.y = 0


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
    [Buttons(upper_frame, "1", button_clicked) for x in range(8)] for y in range(8)
]
for i in range(len(barray)):
    for j in range(len(barray[i])):
        k += 1
        barray[i][j].grid(row=i, column=j, pady=1, padx=1, sticky="NEWS")
        barray[i][j].config(text=str(k))
        barray[i][j].x = i  #x coordinate
        barray[i][j].y = j  #y coordinate
        barray[i][j].v = 0  #visit index
        barray[i][j].h = 0  #heuristics

(i,j) = (8,8)

for i in range(len(barray)):
    for j in range(len(barray[i])):

        count = 0
        for x,y in [(2,1),(2,-1),(-2, 1), (-2, -1), (1,2),(1,-2),(-1, 2), (-1, -2)]:
            #print(i+x,j+y)
            if i+x>=0 and i+x<=7 and j+y>=0 and j+y<=7 and barray[i+x][j+y].h == 0: count += 1
            #if barray[4][4] == 0: count += 1
        print(count," ", end='')
        if j == 7: print("\n")
        

window.geometry("600x600+50+10")
window.minsize(600, 600)
window.mainloop()
