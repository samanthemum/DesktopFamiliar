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

    window.geometry('200x200+'+str(gif.x)+'+'+str(gif.y))
    label.configure(image=frame)
    window.after(1,event, gif)      


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
    
    window.after(150, update, gif)

# CREATE WINDOW FOR PET
window = tk.Tk()
familiar_gif = Gif("bird_familiar")

# CREATE ARRAYS OF FRAMES FOR BUDDY'S ACTIONS
idle = [tk.PhotoImage(file='idle.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.idle_frames)] # idle gif, five frames
idle_to_sleep = [tk.PhotoImage(file='idle_to_sleep.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.idle_to_sleep_frames)]
sleep = [tk.PhotoImage(file='sleeping.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.sleep_frames)]
sleep_to_idle = [tk.PhotoImage(file='sleep_to_idle.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.sleep_to_idle_frames)]
left = [tk.PhotoImage(file='left.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.left_frames)]
right = [tk.PhotoImage(file='right.gif', format = 'gif -index %i' %(i)) for i in range(familiar_gif.right_frames)]

# MAKE BACKGROUND TRANSPARENT
#window.config(highlightbackground='red')
label = tk.Label(window,bd=0,bg='red')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','red')



# ALLOW MOVEMENT AND ANIMATION
label.pack()

# Loop program
window.after(1, event, familiar_gif)
window.mainloop()