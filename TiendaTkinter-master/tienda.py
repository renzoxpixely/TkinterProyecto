from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("Titulo")
window.configure(background='#00304e')

usernameVar = StringVar()
passwordVar = StringVar()


def adminLogin():
    titleLabel = Label(window,text="Sistema de venta",font=("Helvetica", 20),fg="white",background='#00304e')
    titleLabel.grid(row=0,column=0,columnspan=4,padx=(40,0),pady=(10,0))

        
    loginLabel = Label(window,text="Administrador",font=("Helvetica", 15),fg="white",background='#00304e')
    loginLabel.grid(row=1, column=2,padx=(50,0),pady=10)

    usernameLabel = Label(window,text="Usuario",font=("Helvetica", 12),fg="white",background='#00304e')
    usernameLabel.grid(row=2, column=2,padx=20,pady=5)

    passwordLabel = Label(window,text="Contraseña",font=("Helvetica", 12),fg="white",background='#00304e')
    passwordLabel.grid(row=3, column=2,padx=20,pady=5)

    usernameEntry = Entry(window, textvariable=usernameVar)
    usernameEntry.grid(row=2,column=3,padx=20,pady=5)

    passwordEntry = Entry(window, textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3,padx=20,pady=5)

    loginButton=Button(window, text="Iniciar sesion",width=20, height=2,font=("Helvetica", 12),fg="white",background='#2271b3')
    loginButton.grid(row=4, column=2, columnspan=2)    

adminLogin()
window.mainLoop()
