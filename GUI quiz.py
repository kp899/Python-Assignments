from Tkinter import *

the_window = Tk()
the_window.title('Show Checks')

#Def a function to change color when the refresh button is pressed
def changecolor():
    if var1.get():
        f1['background'] = "green"
    else:
        f1['background'] = "grey"
    if var2.get():
        f2['background'] = "green"
    else:
        f2['background'] = "grey"
    if var3.get():
        f3['background'] = "green"
    else:
        f3['background'] = "grey"
    if var4.get():
        f4['background'] = "green"
    else:
        f4['background'] = "grey"
    if var5.get():
        f5['background'] = "green"
    else:
        f5['background'] = "grey"
#Creating an empty frame so that the label frames do not get attached to
#the top of the window
#Using this to make the GUI as close to the provided picture as possible
emptylabel= Frame(height = 2, width = 90)
    
#Make the label frames
f1 = LabelFrame(height = 20, width = 40,background = "grey", relief = 'raised',borderwidth = 1)
f2 = LabelFrame(height = 20, width = 40,background = "grey", relief = 'raised',borderwidth = 1)
f3 = LabelFrame(height = 20, width = 40,background = "grey", relief = 'raised',borderwidth = 1)
f4 = LabelFrame(height = 20, width = 40,background = "grey", relief = 'raised',borderwidth = 1)
f5 = LabelFrame(height = 20, width = 40,background = "grey", relief = 'raised',borderwidth = 1)

#Make a Refresh button
refresh= Button(the_window, text = "Refresh",command = changecolor)

#Writing Variable values for the checkbuttons
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()

#Creating checkbuttons below every label
c1 = Checkbutton(the_window, text = "One",variable = var1)
c2 = Checkbutton(the_window, text = "Two", variable = var2)
c3 = Checkbutton(the_window, text = "Three", variable = var3)
c4 = Checkbutton(the_window, text = "Four", variable = var4)
c5 = Checkbutton(the_window, text = "Five", variable = var5)

#Calling the geometry function to pack everything in a tidy manner
c1.grid(row=3, column=0)
c2.grid(row=3, column=2)
c3.grid(row=3, column=4)
c4.grid(row=3, column=6)
c5.grid(row=3, column=8)
#Packing the emptylabel with a columnspan such that it covers all the labelframes
emptylabel.grid(row =0,column = 0, columnspan = 8)
#Packing the labelframes
f1.grid(row=2, column = 0)
f2.grid(row=2, column = 2)
f3.grid(row=2, column = 4)
f4.grid(row=2, column = 6)
f5.grid(row=2, column = 8)
#Packing the refresh button
refresh.grid(row = 5, column =4)
the_window.mainloop()

