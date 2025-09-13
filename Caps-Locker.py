# No Cap

import pynput, tkinter, random, sys, os
import keyboard as kebab
from pynput import keyboard as pynp_kebab
from pynput.keyboard import Key, Controller
from tkinter import *
from tkinter import messagebox

# Set vars (comme le mot de passe, controller, etc.)
p_o_d = 'PO8BbSmLsf#@12-RFjq5a9q3L!'
pynp_kebab = Controller()
Caps_lock_on = True
time_t = random.randint(5000, 300000)

def x_out():
    window.destroy()

def submit():
    global Caps_lock_on
    password = user_input.get()
    if password == p_o_d:
        Caps_lock_on = False
        kebab.press_and_release('caps_lock')
        kebab.press_and_release('caps_lock')
        messagebox.showinfo(title= 'Congrats!', message = 'Caps lock turned off!')
        x_out()    
         
    else:
        messagebox.showinfo(title = 'Rats!', message = 'Try again :)')

def tap():
    kebab.press_and_release('caps_lock')
    
def monitor():
    if Caps_lock_on and not kebab.is_pressed('caps_lock'):
        tap()
    window.after(100, monitor)

def hide_screen_at_start():
    window.withdraw()
    window.after(time_t, show_window)

def show_window():
    window.deiconify()   

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Screen setup + call functions
window = Tk()
window.title('Capslocker')
window.iconphoto(False, tkinter.PhotoImage(file = resource_path("Capslocker-500500.png")))

submit_button = Button(window, text = 'Submit', command = submit)
submit_button.pack(side = RIGHT)

p_o_d_disp = Button(window, text = "Password:" + p_o_d)
p_o_d_disp.pack()

user_input = Entry() #Define user input object
user_input.pack() #Pack user input widget on window.
user_input.config(font=('Courier New Italic', 50))
user_input.config(bg='black')
user_input.config(fg='green1')
user_input.config(width=25)

tap()
hide_screen_at_start()
monitor()
window.mainloop()


# python -m PyInstaller --onefile --windowed --add-data "Capslocker-500500.png;." Caps-Locker.py