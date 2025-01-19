from tkinter import *
import webbrowser #use to do operations on webbrowser
root=Tk()
root.title("Astral")
def search():
    t=e.get() #gets input from the entry box
    webbrowser.open(t) #used to open the query said by user in entry box in browser
e=Entry(root,font=("Poppins",14,"bold"),width=30,bg="white",fg="red") # here user gives the input to search
e.pack()
b=Button(root,width=10,bg="#974EC3",fg="white",font=("Poppins",20,"bold"),text="Buscar",command=search) #button gives action by command
b.pack()
root.mainloop()