from tkinter import *
top=Tk()
top.geometry("1000x800")
top.title('rohit sharma')
top.config(bg="grey")
welcome=Label(top,text="Welcome To Our Page",font=('TimesNewRoman',20,'bold'),bg="white",fg="black")
welcome.place(x=365,y=100)
def login():
    kit=Frame(top,bg="sky blue",height=700,width=400)
    kit.pack(fill=X)
    label1=Label(kit,text="   ",bg="sky blue",fg="sky blue")
    label1.place(x=300,y=100)
    button=Button(top,text="Sign Up",font=('TimesNewRoman',13,'bold'),bg="red",fg="white",activebackground="violet",activeforeground="yellow",command=login)
    button.place(x=700,y=600,height=50,width=100)
    box=Entry(top,text="",font=('TimesNewRoman',12,'italic'),fg="black")
    box.place(x=365,y=400,width=300,height=30)
    box=Entry(top,text="",font=('TimesNewRoman',12,'italic'),fg="black")
    box.place(x=365,y=300,width=300,height=30)
    welcome=Label(top,text="USERNAME:",font=('TimesNewRoman',12,'bold'),bg="white",fg="black")
    welcome.place(x=250,y=300)
    welcome=Label(top,text="PASSWORD:",font=('TimesNewRoman',12,'bold'),bg="white",fg="black")
    welcome.place(x=250,y=405)
    button=Button(top,text="login",font=('TimesNewRoman',13,'italic'),bg="blue",fg="white",activebackground="violet",activeforeground="yellow",command=login)
    button.place(x=400,y=500,height=50,width=100)
    button=Button(top,text="Sign Up",font=('TimesNewRoman',13,'italic'),bg="red",fg="white",activebackground="violet",activeforeground="yellow",command=login)
    button.place(x=700,y=600,height=50,width=100)
    button=Button(top,text="don't have an account",font=('TimesNewRoman',11,'italic'),bg="red",fg="white",activebackground="violet",activeforeground="yellow",command=login)
    button.place(x=200,y=600,height=50,width=200)
    welcome=Label(top,text="LOGIN PAGE",font=('TimesNewRoman',18,'italic'),bg="white",fg="blue")
    welcome.place(x=350,y=100)

button=Button(top,text="Click Here to Enter Next Page",font=('TimesNewRoman',15,'italic'),bg="blue",fg="white",activebackground="violet",activeforeground="yellow",command=login)
button.place(x=365,y=500,height=40,width=300)
top.mainloop()
          
