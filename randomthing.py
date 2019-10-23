from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("photo tagger")
root.geometry("500x350")

def test(event):
    print(event) #ensure that this line is indented
    topframe = Frame(root,bg='blue',height='20')
    topframe.pack(fill=X) # make as wide as root
    can1 = Canvas(topframe,height='20',width='20',bg="blue",highlightthickness=0)
    can1.create_line(0, 5, 20, 5,fill='white')
    can1.create_line(0, 10, 20, 10,fill='white')
    can1.create_line(0, 15, 20, 15,fill='white')
    can1.bind("<Button-1>",test ) # keyword 
    can1.pack(side=LEFT, padx=5, pady=5)
    