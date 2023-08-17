
import tkinter as tk
from orm.user import User


######################### main TK-WINDOW #########################
window = tk.Tk()
window.title("Mini Social DDD")
window.geometry("500x500")

######################### EVENT BINDING / OBSERVER #########################
def clearWindow(window):
    widgets = window.winfo_children()
    for widget in widgets:
        widget.destroy()

def signIn(event):
    clearWindow(window)

def signUp(event):
    clearWindow(window)
    renderSignUpView(window)

def button_hover(event):
    button = event.widget
    button["bg"] = "gray88"

def button_hover_leave(event):
    button = event.widget
    button["bg"] = "SystemButtonFace"

def register_hover_btn(btn_to_register):
    btn_to_register.bind("<Enter>", button_hover)
    btn_to_register.bind("<Leave>", button_hover_leave)

def createUser(username, email, password):
    try:
        User.create(User.randomId(), username, email, password)
        message = f"Welcome {username}"
    except Exception as e:
        message = f"An error occured with error message:\n{e}"
    finally:
        renderGreetNewCreatedUser(message)

######################### main WIDGETS #########################
def renderGreetNewCreatedUser(message):
    clearWindow(window)
    label_main = tk.Label(window, text=message)
    label_main.place(x=150, y = 100)

def renderSignUpView(window):
    label_main = tk.Label(window, text="CREATE ACCOUNT")
    label_main.place(x=150, y = 100)

    label_username = tk.Label(window, text="Username:")
    label_username.place(x=50, y = 150)
    ent_username = tk.Entry(window)
    ent_username.place(x=150, y=150)

    label_email = tk.Label(window, text="Email:")
    label_email.place(x=50, y = 200)
    ent_email = tk.Entry(window)
    ent_email.place(x=150, y=200)

    label_password = tk.Label(window, text="Password:")
    label_password.place(x=50, y = 250)
    ent_password = tk.Entry(window, show='*')
    ent_password.place(x=150, y=250)

    btn_create = tk.Button(window, text="CREATE")
    btn_create.place(x=150, y=300)
    btn_create.bind('<Button-1>', lambda event: createUser(ent_username.get(), ent_email.get(), ent_password.get()))
    register_hover_btn(btn_create)

def renderMainView(window):
    
    label_main = tk.Label(window, text="RESTRICTED ACCES")
    label_main.place(x=150, y = 100)

    btn_sign_in = tk.Button(window, text="Sign in")
    btn_sign_in.place(x=150, y=150)

    btn_sign_up = tk.Button(window, text="Sign up")
    btn_sign_up.place(x=150, y=200)

    btn_sign_in.bind('<Button-1>', signIn)
    btn_sign_up.bind('<Button-1>', signUp)

    register_hover_btn(btn_sign_in)
    register_hover_btn(btn_sign_up)

    return label_main, btn_sign_in, btn_sign_up


######################### HERE STARTS EXECUTION #########################
mainWidgets = renderMainView(window)
window.mainloop()