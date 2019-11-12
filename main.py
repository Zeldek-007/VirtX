#!/usr/bin/python3
from functions import *
import tkinter as tk
from tkinter import ttk

#Please use Teamviewer 14 for the best experience connecting w/ UDP disabled.

#############################

ports = aggregateOutputDevices()
cPorts = ports[0]
dPorts = ports[1]

xPositions = ['--left-of','--right-of','--above','--below']

#############################

root = tk.Tk()
root.minsize(width=550,height=200)
root.maxsize(width=550,height=200)

#############################

lWidth = tk.Label(text="Width")
lHeight= tk.Label(text="Height")
lHz    = tk.Label(text="@Hz")

lWidth.grid(row=0,column=0)
lHeight.grid(row=0,column=1)
lHz.grid(row=0,column=2)

#############################

tWidth =tk.Entry()
tHeight=tk.Entry()
tHz    =tk.Entry()

tWidth.grid(row=1,column=0)
tHeight.grid(row=1,column=1)
tHz.grid(row=1,column=2)

#############################

dPortsLabel = tk.Label(text="Hijack Port")
dPortsLabel.grid(row=2,column=0)

dPortsCombobox=ttk.Combobox(values=dPorts)
dPortsCombobox.current(0)

dPortsCombobox.grid(row=3,column=0)

#############################

lPosition = tk.Label(text="Position")
lPosition.grid(row=2,column=1)

positionCombobox = ttk.Combobox(values=xPositions)
positionCombobox.current(0)
positionCombobox.grid(row=3,column=1)

#############################

lRelative = tk.Label(text="Relative To")
lRelative.grid(row=2,column=2)

cPortsCombobox=ttk.Combobox(values=cPorts)
cPortsCombobox.current(0)
cPortsCombobox.grid(row=3,column=2)

#############################



#############################

bStartOutput = tk.Button(text="Output!",command=lambda:(pressMe(dPortsCombobox.get(),tWidth.get(),tHeight.get(),tHz.get(),positionCombobox.get(),cPortsCombobox.get())))
bStartOutput.grid(row=8,column=0,columnspan=3)

#############################



#############################

root.mainloop()