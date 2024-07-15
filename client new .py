import socket
from threading import Thread
from tkinter import *
from tkinter import messagebox

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Updated with a valid IP address format
ip_address = '192.168.0.112'
port = 8000

try:
    client.connect((ip_address, port))
    print("Connected with the server...")
except Exception as e:
    print(f"Connection error: {e}")
    messagebox.showerror("Connection Error", "Unable to connect to the server")
    exit()

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300, bg="#17202A")

        self.pls = Label(self.login, text="Please login to continue", justify=CENTER, font="Helvetica 14 bold", bg="#17202A", fg="#EAECEE")
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)
        
        self.labelName = Label(self.login, text="Name: ", font="Helvetica 12", bg="#17202A", fg="#EAECEE")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)
        
        self.entryName = Entry(self.login, font="Helvetica 14", bg="#2C3E50", fg="#EAECEE")
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.go = Button(self.login, text="CONTINUE", font="Helvetica 14 bold", command=lambda: self.goAhead(self.entryName.get()), bg="#ABB2B9")
        self.go.place(relx=0.4, rely=0.55)

        self.Window.mainloop()

    def goAhead(self, name):
        if name:
            self.login.destroy()
            self.layout(name)
            rcv = Thread(target=self.receive)
            rcv.start()
        else:
            messagebox.showerror("Input Error", "Please enter a name")

    def layout(self, name):
        self.name = name
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#17202A")
        
        self.labelHead = Label(self.Window, bg="#17202A", fg="#EAECEE", text=self.name, font="Helvetica 13 bold", pady=5)
        self.labelHead.place(relwidth=1)
        
        self.line =