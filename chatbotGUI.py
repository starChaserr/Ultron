from tkinter import *
import chatBot

x = Tk()

x.title('Ultron AI')
x.geometry('600x415')

chats = StringVar()
message = StringVar()
def uiLoader():
    chats.set("")
    message.set("")
    chats.set("Starting Ultron")
    chats.set(chats.get()+"\n"+ "Ultron is Running")
    view = Label(x,bg="white",fg="blue",textvariable=chats,anchor=SW,height=3,font=("Ariel",12),justify='left')
    view.place(width=600, height=370)

    data = Entry(x,font=("Ariel",12),textvariable= message)
    data.place(width=525,y=370, height=45)

    btn1 = Button(x, text="Send",height=2,command=lambda: getResponse(message.get()),border=4)
    btn1.place(width=75,y=370, x=525)

def getResponse(msg):
    if msg!="":
        message.set("")
        chats.set(chats.get()+"\n"+ "You: "+msg+"\n")
        chats.set(chats.get()+"\n"+ "AI: "+chatBot.responder(msg)+"\n")
    else:
        message.set("Type something...")

uiLoader()
x.mainloop()