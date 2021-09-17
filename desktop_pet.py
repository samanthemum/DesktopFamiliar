import random
import tkinter as tk
import pyautogui

x = 1400
cycle = 0
check = 1
idle_num = [1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'C:\\filepath'

# CYCLE THROUGH FRAMES
def animate(cycle, frames, event_number,first, last):
    if cycle < len(frames) -1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first, last+1,1)
   
    return cycle, event_number
    
# UPDATES THE FRAMES
def update(cycle, check, event_number, x):
    #idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = animate(cycle, idle, event_number,1,9)
        
    #idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = animate(cycle, idle_to_sleep, event_number,10,10)
        
    #sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = animate(cycle, sleep, event_number,10,15)
        
    #sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = animate(cycle, sleep_to_idle, event_number,1,4)
        
    # walk towards right
    elif check == 5:
        frame = right[cycle]
        cycle, event_number = animate(cycle, right, event_number,1,9)
        x += 3
       
     # walk towards left
    elif check == 4:
        frame = left[cycle]
        cycle, event_number = animate(cycle, left, event_number,1,9)
        x -= 3

    window.geometry('100x100+'+str(x)+'+1050')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x)      


def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)

    elif event_number == 5:
        check = 1
        print('from_idle_to_sleep')
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in walk_left:
        check = 4
        print('walking left')
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in walk_right:
        check = 5
        print('walking right')
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in sleep_num:
        check = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x)

    elif event_number == 14:
        check = 3
        print('sleep to idle')
        window.after(1000, update, cycle, check, event_number, x)

# CREATE WINDOW FOR PET

window = tk.Tk();

# CREATE ARRAYS OF FRAMES FOR BUDDY'S ACTIONS
idle = [tk.PhotoImage(file='idle.gif', format = 'gif -index %i' %(i)) for i in range(5)] # idle gif, five frames
idle_to_sleep = [tk.PhotoImage(file='idle_to_sleep.gif', format = 'gif -index %i' %(i)) for i in range(8)]
sleep = [tk.PhotoImage(file='sleeping.gif', format = 'gif -index %i' %(i)) for i in range(3)]
sleep_to_idle = [tk.PhotoImage(file='sleep_to_idle.gif', format = 'gif -index %i' %(i)) for i in range(8)]
left = [tk.PhotoImage(file='left.gif', format = 'gif -index %i' %(i)) for i in range(8)]
right = [tk.PhotoImage(file='right.gif', format = 'gif -index %i' %(i)) for i in range(8)]

# MAKE BACKGROUND TRANSPARENT
window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

# ALLOW MOVEMENT AND ANIMATION
label.pack()

# Loop program
window.after(1,event,cycle,check,event_number,x)
window.mainloop()