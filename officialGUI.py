from tkinter import *
from tkinter import messagebox
from datetime import datetime
import requests
from PIL import ImageTk,Image

root = Tk()
root.title("Mental Health App")
g_color = "#008000"
#frame

KINTONE_API_TOKEN = "8hQsGq3Gzn2SC7HIqGbWcyXu75sWybbPisVjIDCi"
KINTONE_API_URL = "https://t368el6r8vkl.kintone.com/k/v1/record.json"
APP_ID = "1"


#creating the image
pre_img = ImageTk.PhotoImage(Image.open("brain.png"))
#making the image
brain_img = Label(image=pre_img)
brain_img.grid(row=1, column=6)

#drop down menu
itemchose = StringVar()
items = [
    "Happy",
    "Anxious",
    "Stressed",
    "Sad",
    "Depressed",
    "Neutral",
    "Angry"
    ]
drop = OptionMenu(root, itemchose, *items)



#Labels
space_l = Label(root, text=' ')
space_l.grid(row=0, column=0)
w_label = Label(root, text="Welcome to the Mental Health Application!", fg=g_color)
w_label.grid(row=0, column=5, columnspan=3)
m_label = Label(root, text="Mood:")
enterm_label = None
explain_e = Entry(root, width=30)
explain_e.insert(0, "Explain why you are feeling this way")
better_l = Label(root, text="What can you do better tomorrow?")
better_e = Entry(root, width=10)
goal_l = Label(root, text="What is one goal you want to accomplish tomorrow?")
goal_e = Entry(root, width=10)
save_kintone = Button(root, text="Save to Kintone", fg=g_color)
date_e = Entry(root)
date_e.insert(0, "Enter Date")

#function to send to kintone
def send_to_kintone(date, mood, explanation, how_to_improve, goals):
    """Send data to kintone."""
    current_datetime = "2024-12-27T12:00:00Z"
    headers = {
        "X-Cybozu-API-Token": "8hQsGq3Gzn2SC7HIqGbWcyXu75sWybbPisVjIDCi",
        "Content-Type": "application/json",
    }
    data = {
        "app": "1",
        "record": {
            "Created_datetime": {"value": current_datetime},
            "Drop_down": {"value": mood},
            "Text": {"value": explanation},
            "Text_0": {"value": how_to_improve},
            "Text_1": {"value": goals},
        },

    }
    try:
        response = requests.post(KINTONE_API_URL, headers=headers, json=data)
        response.raise_for_status()
        messagebox.showinfo("Success", "Data sent to Kintone successfully!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to send data to Kintone: {e}")


#start funtion
def startapp():
    global w_label
    global start_b
    global brain_img
    global drop
    global items
    global itemchose
    global m_label
    global button_back
    global button_forward
    brain_img.grid_forget()
    start_b.grid_forget()
    w_label.grid_forget()
    date_e.grid(row=1, column=0, sticky="w")
    drop.grid(row=1, column=3)
    m_label.grid(row=1, column=2)
    enter_b.grid(row=1, column=4)
    button_back.grid(row=20, column=0)
    button_forward.grid(row=20, column=2)

def entermood():
    global enterm_label
    if enterm_label is not None:
        enterm_label.grid_forget()
    enterm_label = Label(root, text="Why are you feeling " + itemchose.get() + " today?")
    enterm_label.grid(row=2, column=0, sticky="w")
    explain_e.grid(row=3, column=0, sticky="w")



enterm_label = Label(root, text="Why are you feeling " + itemchose.get() + " today?")

#Buttons

start_b = Button(root, text="Start", command=startapp, fg=g_color)
start_b.grid(row=2, column=5, columnspan=6)
enter_b = Button(root, text="Enter Mood", fg=g_color, command=entermood)


def collect_input():
    date_collect = date_e.get()
    mood_collect = itemchose.get()
    explain_collect = explain_e.get()
    better_collect = better_e.get()
    goal_collect = goal_e.get()

    if not date_collect or not mood_collect or not explain_collect or not better_collect or not goal_collect:
        messagebox.showerror("Error", "All fields are required")
        return
    send_to_kintone(date_collect, mood_collect, explain_collect, better_collect, goal_collect)
#functions
def forward():
    global button_forward
    global button_back
    global w_label
    global start_b
    global brain_img
    global drop
    global items
    global itemchose
    global m_label
    global enterm_label
    global explain_e
    global better_l
    global better_e
    global goal_l
    global goal_e
    global save_kintone
    enterm_label.grid_forget()
    explain_e.grid_forget()
    date_e.grid_forget()
    drop.grid_forget()
    m_label.grid_forget()
    enter_b.grid_forget()
    save_kintone = Button(root, text="Save to Kintone", fg=g_color, command=collect_input)
    save_kintone.grid(row=20, column=1)
    better_l.grid(row=0, column=0)
    better_e.grid(row=0, column=1)
    goal_l.grid(row=1, column=0)
    goal_e.grid(row=1, column=1)


    button_back = Button(root, text="<<", command=back, fg=g_color)
    button_forward = Button(root, text=">>", state=DISABLED)
    button_back.grid(row=20, column=0)
    button_forward.grid(row=20, column=2)




def back():
    global w_label
    global start_b
    global brain_img
    global drop
    global items
    global itemchose
    global m_label
    global enterm_label
    global explain_e
    global better_l
    global better_e
    global goal_l
    global goal_e
    global button_forward
    global button_back
    global save_kintone
    better_l.grid_forget()
    better_e.grid_forget()
    goal_l.grid_forget()
    goal_e.grid_forget()
    save_kintone.grid_forget()
    date_e.grid(row=1, column=0, sticky="w")
    drop.grid(row=1, column=3)
    m_label.grid(row=1, column=2)
    enter_b.grid(row=1, column=4)


    button_forward = Button(root, text=">>", command=forward, fg=g_color)
    button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=20, column=0)
    button_forward.grid(row=20, column=2)






#buttons
button_back = Button(root, text="<<", fg=g_color, command=lambda: back, state=DISABLED)
button_forward = Button(root, text=">>", fg=g_color, command=forward)



#exit button
exit_b = Button(root, text="Exit Application", command=quit, fg=g_color)
exit_b.grid(row=20, column=5, columnspan=6)
root.mainloop()