from msilib.schema import RadioButton
import random
import tkinter as tk
import pyautogui
from gif import *

# CYCLE THROUGH FRAMES
def animate(gif, frames, first, last):
    if gif.cycle < len(frames) -1:
        gif.cycle += 1
    else:
        gif.cycle = 0
        gif.event_number = random.randrange(first, last+1,1)
   
    return gif.cycle, gif.event_number
    
# UPDATES THE FRAMES
def update(gif):
    #idle
    if gif.check == 0:
        frame = idle[gif.cycle]
        gif.cycle, gif.event_number = animate(gif, idle,1,9)
        
    #idle to sleep
    elif gif.check == 1:
        frame = idle_to_sleep[gif.cycle]
        gif.cycle, gif.event_number = animate(gif, idle_to_sleep,10,10)
        
    #sleep
    elif gif.check == 2:
        frame = sleep[gif.cycle]
        gif.cycle, gif.event_number = animate(gif, sleep, 10,15)
        
    #sleep to idle
    elif gif.check == 3:
        frame = sleep_to_idle[gif.cycle]
        gif.cycle, gif.event_number = animate(gif, sleep_to_idle, 1,4)
        
    # walk towards right
    elif gif.check == 5:
        frame = right[gif.cycle]
        gif.cycle, gif.event_number = animate(gif, right, 1,9)
        gif.x += 3
        gif.y += random.randint(-3, 3)
       
     # walk towards left
    elif gif.check == 4:
        frame = left[gif.cycle]
        cycle, event_number = animate(gif, left, 1, 9)
        gif.x -= 3
        gif.y += random.randint(-3, 3)

    familiar_window.geometry('500x500+'+str(gif.x)+'+'+str(gif.y))
    label.configure(image=frame)
    familiar_window.after(1,event, gif)      


def event(gif):
    if gif.event_number in gif.idle_num:
        gif.check = 0

    elif gif.event_number == gif.idle_to_sleep_num:
        gif.check = 1

    elif gif.event_number in gif.walk_left:
        gif.check = 4

    elif gif.event_number in gif.walk_right:
        gif.check = 5

    elif gif.event_number in gif.sleep_num:
        gif.check = 2

    elif gif.event_number == gif.sleep_to_idle_num:
        gif.check = 3
    
    familiar_window.after(150, update, gif)

def name_entered():
    entered_name = name_input.get("1.0", "end-1c")
    familiar_gif.name = entered_name
    familiar_type = var.get()
    print(familiar_type)
    familiar_gif.setType(familiar_type)
    save_familiar()
    prompt_window.destroy()

def create_new_familiar():
    main_window.destroy()
    global new_familiar
    new_familiar = True

def use_old_familiar():
    save_file = open("save_data.txt", "r")
    if save_file.closed:
        print("Error opening file")
        create_new_familiar()
    
    familiar_name = save_file.readline()[:-1]
    familiar_type = save_file.readline()[:-1]

    if familiar_type != "bird_familiar" and familiar_type != "goat_familiar":
        print(familiar_name)
        print(familiar_type)
        print("Invalid data in file")
        create_new_familiar()

    familiar_gif.name = familiar_name
    familiar_gif.setType(familiar_type)
    main_window.destroy()


def save_familiar():
    save_file = open("save_data.txt", "w")
    save_file.write(familiar_gif.name + "\n")
    save_file.write(familiar_gif.type + "\n")
    save_file.close()


# CREATE OBJECT FOR FAMILIAR
familiar_gif = Gif("bird_familiar")
new_familiar = False

# MAIN WINDOW
main_window = tk.Tk()
main_window.geometry("800x800")
main_window.title("DesktopFamiliar")
main_create_new = tk.Button(main_window, height=2, width=20, text = "Create new familiar",command=lambda: create_new_familiar())
main_create_new.pack()
main_use_old = tk.Button(main_window, height=2, width=20, text = "Use previous familiar",command=lambda: use_old_familiar())
main_use_old.pack()
main_window.mainloop()

# ASK USER FOR FAMILIAR NAME
if new_familiar:
    prompt_window = tk.Tk()
    prompt_window.geometry("800x800")
    prompt_window.title("DesktopFamiliar")

    var = tk.StringVar()
    var.set("bird_familiar")

    species_label = tk.Label(text = "Choose the species of your familiar companion.")
    bird_button = tk.Radiobutton(prompt_window,text="Bird",value="bird_familiar",variable=var)
    goat_button = tk.Radiobutton(prompt_window,text="Goat",value="goat_familiar",variable=var)
    species_label.pack()
    bird_button.pack()
    goat_button.pack()

    name_label = tk.Label(text = "Name your familiar companion.")
    name_input = tk.Text(prompt_window, height=10, width=25, bg = "white")
    name_button = tk.Button(prompt_window, height=2, width=20, text="Enter",command=lambda:name_entered())
    name_label.pack()
    name_input.pack()
    name_button.pack()
    prompt_window.mainloop()

# CREATE WINDOW FOR PET
familiar_window = tk.Tk()

# CREATE ARRAYS OF FRAMES FOR BUDDY'S ACTIONS
print(familiar_gif.type)
if familiar_gif.type == "bird_familiar":
    idle = [tk.PhotoImage(file='idle.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.idle_frames)] # idle gif, five frames
    idle_to_sleep = [tk.PhotoImage(file='idle_to_sleep.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.idle_to_sleep_frames)]
    sleep = [tk.PhotoImage(file='sleeping.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.sleep_frames)]
    sleep_to_idle = [tk.PhotoImage(file='sleep_to_idle.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.sleep_to_idle_frames)]
    left = [tk.PhotoImage(file='left.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.left_frames)]
    right = [tk.PhotoImage(file='right.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.right_frames)]

elif familiar_gif.type == "goat_familiar":
    idle = [tk.PhotoImage(file='goat_idle.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.idle_frames)] 
    idle_to_sleep = [tk.PhotoImage(file='goat_idle_to_sleep.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.idle_to_sleep_frames)]
    sleep = [tk.PhotoImage(file='goat_sleep.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.sleep_frames)]
    sleep_to_idle = [tk.PhotoImage(file='goat_sleep_to_idle.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.sleep_to_idle_frames)]
    left = [tk.PhotoImage(file='goat_left.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.left_frames)]
    right = [tk.PhotoImage(file='goat_right.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.right_frames)]

# MAKE BACKGROUND TRANSPARENT
#window.config(highlightbackground='red')
label = tk.Label(familiar_window,bd=0,bg='red', padx=10, pady=10)
familiar_window.overrideredirect(True)
familiar_window.configure(bg='red')
familiar_window.wm_attributes('-transparentcolor','red')
familiar_name = tk.Label(text=familiar_gif.name, padx=10, pady=10)



# ALLOW MOVEMENT AND ANIMATION
if familiar_gif.name != '':
    familiar_name.pack()
label.pack()

# Loop program
familiar_window.after(1, event, familiar_gif)
familiar_window.mainloop()