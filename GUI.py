from tkinter import *
from PIL import ImageTk,Image
#setup
root = Tk()
root.geometry("1000x900")
root.title("Mood Tracker")
#date entry
Date = Label(root, text="Date: ").grid(row=0, column=0)
date_entry = Entry(root, width=10)
date_entry.grid(row=0, column=1)

#images
#happy
happy = ImageTk.PhotoImage(Image.open("happyGUI.jpg"))
label = Label(image=happy)
label.grid(row=2, column=1)

emotelabel = Label(root, text="What emotion are you feeling today?")
emotelabel.grid(row=1, column=0)




#drop down boxes
clicked = StringVar() #variable

optionse = [
    "Happy",
    "Sad",
    "Angry",
    "Neutral"
]

clicked.set(optionse[0])
drop = OptionMenu(root, clicked, *optionse) #clicked is a variable we store the chosen item
drop.grid(row=1, column=1)

def show():
    showlabel = Label(root, text="You're feeling: "+clicked.get()+" on "+date_entry.get())
    showlabel.grid(row=3, column=1)

button = Button(root, text="Show Emotion", command=show)
button.grid(row=1, column=2)


#exit button
exit = Button(root, text="Exit", command=root.quit)
exit.grid(row=5, column=1)
root.mainloop()

#make the spaces between the label and dropdown menu smaller
#make the image smaller and learn to resize
#name each image, and make a image viewer each time you clikc it shows different emotions coreesponding to each imge
#get data back, date/time, emotion, text they input
#how to get the week's data back