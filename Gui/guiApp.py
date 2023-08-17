import tkinter as tk

window = tk.Tk()
window.title("Mini Social DDD")
window.geometry("500x500")

# add widgets
label_main = tk.Label(window, text="Restricted Access")
label_main.place(x=150, y = 100)

btn_sign_in = tk.Button(window, text="Sign in")
btn_sign_in.place(x=150, y=150)

btn_sign_up = tk.Button(window, text="Sign up")
btn_sign_up.place(x=150, y=200)

# event binding / Observer
def signIn(event):
    print("Show sign in page")
    print(event)

def signUp(event):
    print("Show sign up page")
    print(event)


btn_sign_in.bind('<Button-1>', signIn)
btn_sign_up.bind('<Button-1>', signUp)

def button_hover(event):
    button = event.widget
    button["bg"] = "gray88"

def button_hover_leave(event):
    button = event.widget
    button["bg"] = "SystemButtonFace"

def register_hover_btn(btn_to_register):
    btn_to_register.bind("<Enter>", button_hover)
    btn_to_register.bind("<Leave>", button_hover_leave)

register_hover_btn(btn_sign_in)
register_hover_btn(btn_sign_up)

window.mainloop()