import tkinter as tk
import tkinter.messagebox as tkmsb
from tkinter.filedialog import *
from randomizer import randomize
from sys import platform
import os

def send_values():
    loop=int(blocks.get())
    name=string.get()
    start=starttype.get()
    template = templatevar.get()
    try:
        cpnum = randomize(name, loop, start, template)
    except Exception as e:
        tkmsb.showerror("TMTrackRandomizer", "Error!\n" + str(e) + "\nPlease report this to the developer!")
        exit()
    tkmsb.showinfo('TMTrackRandomizer', 'Done! Number of Checkpoints : '+cpnum)

#Linux problem...
if platform == linux:
    os.environ['DISPLAY'] = "unix$DISPLAY"
    
#GUI START
root = tk.Tk("TMTrackRandomizer")
text = tk.Label(root, text="Choose the name of your map: ")
text.grid(row=1, column=1)
string = tk.StringVar() 
string.set("RandomizedMap")
mapname = tk.Entry(root, textvariable=string, width=20)
mapname.grid(row=1, column=3)
templatevar = tk.StringVar()
templatevar.set("Template.Challenge.Gbx")
templatebutton = tk.Button(root, text="Select a template", command=lambda:templatevar.set(askopenfilename()))
text3 = tk.Label(root, textvariable=templatevar)
templatebutton.grid(row=2,column=1)
text3.grid(row=2, column=2, columnspan=2)
text1 = tk.Label(root, text="Choose a number of blocks: ")
text1.grid(row=3, column=1)
blocks = tk.Spinbox(root, from_=2, to=9999999999, width=18)
blocks.grid(row=3, column=3)
starttype = tk.StringVar() 
starttype.set("0")
text2 = tk.Label(root, text="Choose the type of the start block: ")
normal = tk.Radiobutton(root, text="Normal", variable=starttype, value=0)
multilap = tk.Radiobutton(root, text="Multilap", variable=starttype, value=1)
text2.grid(row=4, column=1)
normal.grid(row=4, column=2)
multilap.grid(row=4, column=3)

button=tk.Button(root, text="Randomize!", command=send_values)
button.grid(row=5,column=2)
root.mainloop()
#GUI END
