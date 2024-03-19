#Login page for Alpha tours and travels

from tkinter import *
from functools import partial
from PIL import Image,ImageTk
import tkinter as tk


def validateLoginalphatravels(username, password):#to get the password entered
	print("username entered :", username.get())
	print("password entered :", password.get())
  
    
def on_resize(event):#setting for background image  
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)


Window =tk.Tk()  #setting geometry for the window pop up
Window.geometry('890x760')  
Window.title('ALPHA TOURS AND TRAVELS')

bgimg = Image.open('alpha.png') #opening the local image
l =tk.Label(Window)
l.place(x=0, y=0, relwidth=1, relheight=1)
l.bind('<Configure>', on_resize) 
#different labels
username88Label = Label(Window, text="ALPHA TOURS AND TRAVELS LOGIN",bg='orange',font=('Franklin Gothic Book',15,'italic')).grid(row=1, column=906)


usernameLabel = Label(Window, text="Username",bg='lightblue',font=('Franklin Gothic Book',15,'bold')).grid(row=100, column=100)
username = StringVar()
usernameEntry = Entry(Window, textvariable=username,font=('Franklin Gothic Book',15,'bold')).grid(row=100, column=110)  

#in-built function show="*" to hide password while entering 
passwordLabel = Label(Window,text="Password",bg='lightblue',font=('Franklin Gothic Book',15,'bold')).grid(row=200, column=100)  
password = StringVar()
passwordEntry = Entry(Window, textvariable=password, show='*',font=('Franklin Gothic Book',15,'bold')).grid(row=200, column=110)  

validateLoginalphatravels = partial(validateLoginalphatravels, username, password)

loginButton = Button(Window, text="Login",bg='yellow',font=('Franklin Gothic Book',15,'bold'), command=validateLoginalphatravels).grid(row=500, column=100) 
RegisterButton = Button(Window, text="Register Now!",bg='yellow',font=('Franklin Gothic Book',15,'bold')).grid(row=600, column=100) 


Window.mainloop()
