import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


IP_ADDRESS='127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE=4096


 


def musicWindow():
    window=Tk()
    window.title("MUSIC WINDOW")
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectSong=Label(window,text="Select Song",bg="LightSkyBlue",font=("Calibri",10))
    selectSong.place(x=2,y=9)

    listBox=Listbox(window,height = 10,width = 38,activestyle = 'dotbox',bg="LightSkyBlue",borderwidth=4, font = ("Calibri",10))
    listBox.place(x=15,y=30)


    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listBox.yview)

    playButton=Button(window,text="Play",bd=1,width=10,bg="SkyBlue", font = ("Calibri",10))
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="Stop",bd=1,width=10,bg="SkyBlue", font = ("Calibri",10))
    stopButton.place(x=200,y=200)

    upload=Button(window,text="Upload",bd=1,bg="SkyBlue",width=10, font = ("Calibri",10))
    upload.place(x=30,y=250)

    download=Button(window,text="Download",bd=1,bg="SkyBlue",width=10, font = ("Calibri",10))
    download.place(x=200,y=250)

    infolabel=Label(window,text="",fg="blue",font=("Calibri",10))
    infolabel.place(x=3,y=300)



    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()
