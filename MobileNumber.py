from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = Tk()
window.geometry("500x500")
window.title("Mobile Number File Store Module")
window.configure(bg="#3B7A57")

#FUNCTION TO INSERT DETAILS IN TEXT FILE
def insertdetails():
    insert_name = str(Name_entery.get())
    insert_number = str(Number_entery.get())

#IF THE LENGTH OF NUMBER IS EQUAL TO 10
    if len(insert_number) == 10:
        check = open('number.txt','a')
        check1 = open('number.txt','r')
        test = check1.read()

#IF NUMBER IS ALREADY PRESENT IN THE TEXT FILE
        if insert_number in test:
            messagebox.showwarning("Duplicate","Number Already Exists")

#TO INSERT NEW DETAILS
        else:
            check.write(f"{insert_name} - \t\t{insert_number}\n")
            messagebox.showinfo("Information","Details inserted")

#IF DETAILS ARE NOT INSERTED PROPERLY BEFORE PRESSING INSERT BUTTON
    elif insert_number == str(insert_number):
        messagebox.showwarning("Error","Enter the correct Details")
    Name_entery.delete(0,100)
    Number_entery.delete(0,100)


#FUNCTION TO CHECK THE DETAILS
def viewdetails():
    check = open('number.txt', 'r')
    rest = check.read()
    for a in rest[::-1]:
        Check_details.insert(0.0, a)

#FUNCTION TO CLEAR THE DETAILS
def cleardetails():
    Name_entery.delete(first=0,last=100)
    Number_entery.delete(first=0,last=100)
    Check_details.delete(0.0,100.0)

#PFUNCTION TO EXIT THE WINDOW
def exitwindow():
    window.destroy()

#LABEL OF HEADING
Title_of_the_form=Label(window,text="ENTER YOUR INFORMATION HERE",fg="black",bg="#479469",relief="solid",font=("arial",19,"bold"))
Title_of_the_form.place(x=35,y=10)

#LABEL OF NAME
Name_label=Label(window,text=" NAME: ",fg="black",bg="#479469",relief="solid",font=("arial",15))
Name_label.place(x=35,y=55)

#ENTRY FIELD OF NAME
Name_entery=Entry(window)
Name_entery.place(x=150,y=55)

#LABEL OF NUMBER
Number_label=Label(window,text=" NUMBER: ",fg="black",bg="#479469",relief="solid",font=("arial",15))
Number_label.place(x=35,y=100)

#ENTRY FIELD OF NUMBER
Number_entery=Entry(window)
Number_entery.place(x=150,y=100)


#BUTTON FOR INSERTING  DETAILS
Insert_details_button=Button(window, text="INSERT", width=12, fg="black", bg="#7affb5", font=("bold",15), command=insertdetails)
Insert_details_button.place(x=150,y=150)

#LABEL OF VIEW DETAILS
View_details_label=Label(window,text="VIEW YOUR DETAILS HERE",fg="black",bg="#479469",relief="solid",font=("arial",15,"bold"))
View_details_label.place(x=100,y=200)

#VIEW AREA OF DETAILS
Check_details=tk.Text(window, fg="black", bg="#479469", relief="solid", width=38, height=5,font=("bold"))
Check_details.place(x=35, y=250)

#VIEW INFORMATION ENTERD BUTTON
Check_details_button=Button(window, text="CHECK", width=12, fg="black", bg="#7affb5", font=("bold",15), command=viewdetails)
Check_details_button.place(x=130,y=400)

#CLEAR BUTTON
Clear_details_button=Button(window,text="CLEAR",width=12,fg="white",bg="#bd0000",font=("bold",15),command=cleardetails)
Clear_details_button.place(x=290,y=400)

#EXIT BUTTON
Exit_button=Button(window,text="EXIT",width=12,fg="white",bg="#ff0000",font=("bold",15),command=exitwindow)
Exit_button.place(x=170,y=450)

window.mainloop()