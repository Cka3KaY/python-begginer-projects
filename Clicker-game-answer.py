from tkinter import *
#window
window = Tk()
window.geometry("300x300")
window.title("clicker game")  
window.config(background="orange")
your_gay = Label(text="⬆⬆⬆⬆⬆⬆", font="comic", pady=5)


def your():
    window.config(background="blue")
    your_gay.config(font=('Helvetica bold', 40),
                    text="Hello world", pady=50, 
                    background="dark blue",
                     foreground="orange")
    Button.destroy()
    my_Label.destroy()


my_Label = Label(window, text="press this button", padx=40)
my_Label.pack()


Button = Button(window,
                text="<click me>",
                font=("Comic Sans",30),
                command=your, padx=40, pady=2)


Button.pack()
your_gay.pack()


    

window.mainloop()
