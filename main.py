from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image

root = Tk()
root.geometry("680x510")

# Menu bar is created at the top of window
MainMenu = Menu(root)
m1 = Menu(MainMenu, tearoff=0)
m1.add_command(label="Register Members")

m1.add_command(label="Manage Apponitment")
# m1.add_command(label="Book Vaccination Slots")
m1.add_separator()  # add_commmand() function will add horizontal line.
m1.add_command(label="Download Certificate")

m2 = Menu(MainMenu, tearoff=0)  # tearoff = 0 will remove creating sub menu.
m2.add_command(label="Co-WIN International")
m2.add_command(label="Vaccinator")
m2.add_command(label="Department Login")
m2.add_separator()
m2.add_command(label="Verify Certificate")
m2.add_separator()
m2.add_command(label="Vaccination Statistics")

m3 = Menu(MainMenu, tearoff=0)
m3.add_command(label="Frequently Asked Questions")
m3.add_separator()
m3.add_command(label="Certificate Corrections")

root.config(menu=MainMenu)  # config(menu=MainMenu) will add main menu in tkinter window.
MainMenu.add_cascade(label="Vaccination Services",
                     menu=m1)  # MainMenu.add_cascade() function will add menu in main menu.
MainMenu.add_cascade(label="Platforms", menu=m2)
MainMenu.add_cascade(label="Suppport", menu=m3)

#  Frame is used to give heading
root.title("Vaccine Registration ")
hedf=Frame(root,bg="#EEEE48",height=45).pack(side=TOP,fill='both')
heading=Label(hedf,text="Vaccine Registration",font="TIMES 25 bold",fg="#0000e6",bg="#EEEE48").place(x=200)
# button is used
log_button = Button(root,text="Let's Get Vaccinated",font = "TIMES 15 bold",fg= "#0000e6",bg="#EEEE48",command=lambda:[letsgetv()]).place(x=220,y=360)

# img = PhotoImage(file="cowin.gif")
# l=Label(root,image=img)
# l.pack(pady=15)
# button is used
review_but = Button(root,text="Share Your Vaccination Experience ",font = "TIMES 15 bold",fg= "#0000e6",bg="#EEEE48",command=lambda: [text_review()]).place(x=160,y=420)

quote = Label(root,text="Make your conttribution in the fight against COVID-19. Get Vaccinated",font="Times 16 bold",bg="#ffb380",fg= "#0000e6").place(x=9,y=320)
global text_win
# this function  used to bring textarea when called
def text_review():
    text_win = Toplevel(root)
    text_win.geometry("520x350")
    t = Text(text_win, height=5, width=50, fg="red", font="Times ")
    t.pack(pady=20)
    submit = Button(text_win,text="Submit",font = "TIMES 15 bold",fg= "#0000e6",bg="#EEEE48").place(x=210,y=180)
    text_win.configure(bg="#ffb380")

# this function clears the entry when called
def OK():
    na=v1.get()
    ag=v2.get()
    adn=v3.get()
    mob=v4.get()
    pi=v5.get()
    if (na == "" or ag == "" or adn == "" or mob == "" or pi == ""):
        messagebox.showinfo("", "Blank not alloed")

    elif (na == "Rohit" or adn == 9856):  # If Rohit vaccinated then generates message..
        messagebox.showinfo("Message", " is already vaccinated.")

global v1
global v2
global v3
global v4
global v5

# this function takes input from user like name ,age ,adhar card number etc. when called
def letsgetv():
    top = Toplevel(root)
    top.geometry("500x450")
    frm1 = Frame(top, bg="#EEEE48", height=45).pack(side=TOP, fill='both')
    head = Label(top, text="Vaccine Registration", font="TIMES 25 bold", fg="#0000e6", bg="#EEEE48").place(x=120)
    #  text box is used to take input
    nm = StringVar()
    name = Label(top, text="Name", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=50)
    v1 = Entry(top)
    v1.place(x=190, y=50)



    age = Label(top, text="Age", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=80)
    v2 = Entry(top)
    v2.place(x=190, y=80)


    aadharno = Label(top, text="AADHAR NUMBER", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=110)
    v3 = Entry(top)
    v3.place(x=190, y=110)
    v3.config(show="*")

    mob_no = Label(top, text="MOBILE NUMBER", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=140)
    v4 = Entry(top)
    v4.place(x=190, y=140)

    pin = Label(top, text="PIN", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=170)
    v5 = Entry(top)
    v5.place(x=190, y=170)

    gender = Label(top, text="GENDER", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=200)

    rd1 = StringVar()
    # radiobutton are used to select from multiple values
    rb1 = Radiobutton(top, text="MALE", variable=rd1, value='Male', bg='#ffb380',fg= "#0000e6",font="Times 13 bold")
    rb1.place(x=180, y=200)
    rb2 = Radiobutton(top, text="FEMALE", variable=rd1, value='Female', bg='#ffb380',fg= "#0000e6",font="Times 13 bold")
    rb2.place(x=260, y=200)
    rb3 = Radiobutton(top, text="OTHER", variable=rd1, value='Other', bg='#ffb380',fg= "#0000e6",font="Times 13 bold")
    rb3.place(x=360, y=200)

    # button
    butt = Button(top, text="Login", height=1, width=5,command=lambda: [onClick(),OK(),clear_text()],bg='#EEEE48',fg='#0000e6',font="times 13 bold").place(x=250, y=270)
    top.configure(bg='#ffb380')
    # this function is used to take input like dose name , state ,city,date
    def onClick():
        left = Toplevel(top)
        left.geometry("550x350")
        left.title("Appointment Slip")
        frm3 = Frame(left, bg="#EEEE48", height=45).pack(side=TOP, fill='both')
        bb=Label(left,text="Vaccine Registration" , font="TIMES 25 bold", fg="#0000e6", bg="#EEEE48").place(x=120)

        dose = Label(left, text="DOSE", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=50)
        rd2 = StringVar()
        rb4 = Radiobutton(left, text="FIRST", variable=rd2, value='FIRST', bg='#ffb380',fg= "#0000e6",font="Times 13 bold")
        rb4.place(x=110, y=50)
        rb5 = Radiobutton(left, text="SECOND", variable=rd2, value='SECOND', bg='#ffb380',fg= "#0000e6",font="Times 13 bold")
        rb5.place(x=210, y=50)
        st = Label(left, text="STATE", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=95)
        menu1 = StringVar()
        menu1.set("Select State")
        # drop down menu is created for state
        lists = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar ", "Chhattisgarh", "Goa","Gujarat", "Haryana", "Jharkhand", "Maharashtra", "Madhya Pradesh", "Karnatak", "Kerela", "Tamil Nadu", "Odissa", "West Bengal"]

        drop1 = OptionMenu(left, menu1,*lists)
        drop1.place(x=85, y=95)
        # city
        # drop down menu is created for city
        cit = Label(left, text="City", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=205, y=95)
        menu2 = StringVar()
        menu2.set("Select City")
        listc = ["Vadodara", "Ahmadabad", "Surat", "Rajkot", "Anand", "Gandhi Nagar", "Bhavnagar"]
        # Create a dropdown Menu
        drop2 = OptionMenu(left, menu2,*listc )
        drop2.place(x=245, y=95)
        left.configure(bg='#ffb380', bd='0')

        # radiobutton is used to select vaccine name
        lk = StringVar()
        Vaccine = Label(left,text="VACCINE", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=185)
        lk1 = Radiobutton(left, text= "Covaxin", variable=lk, value='Covaxin', bg='#ffb380', fg="#0000e6",font="Times 13 bold")
        lk1.place(x=110, y=180)
        lk2 = Radiobutton(left, text= "Covishield", variable=lk, value='Covishield', bg='#ffb380', fg="#0000e6",font="Times 13 bold")
        lk2.place(x=210, y=180)


        date = Label(left, text="DATE ", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10, y=145)
        lab=Entry(left)
        lab.place(x=90,y=145)
        but2 = Button(left, text="Book Slot", height=1,bg='#EEEE48',fg='#0000e6',font="times 13 bold",command=lambda: [appt_slip()]).place(x=45, y=230)

        # this function prints the value entered by user in earlier windows
        def appt_slip():
            slip = Toplevel(left)
            slip.geometry("550x350")
            frm4 = Frame(slip,bg='#EEEE48',height=45).pack(side=TOP, fill='both')
            lb4=Label(slip,text="Appointment Slip", font="TIMES 25 bold", fg="#0000e6", bg="#EEEE48").place(x=200)
            slip.configure(bg="#ffb380")
            ap_name = Label(slip,text="Name : ", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10,y=70)
            pn=Label(slip,text=v1.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80,y=70)
            ap_age = Label(slip,text="Age : ", bg='#ffb380',fg= "#0000e6",font="Times 13 bold").place(x=10,y=100)
            pa = Label(slip, text=v2.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=100)
            ap_gen = Label(slip, text="Gender : ", bg='#ffb380', fg="#0000e6", font="Times 13 bold").place(x=10, y=130)
            pg = Label(slip, text=rd1.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=130)

            ap_dose = Label(slip, text="Dose : ", bg='#ffb380', fg="#0000e6", font="Times 13 bold").place(x=10, y=160)
            pd = Label(slip, text=rd2.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=160)

            ap_state = Label(slip, text="State : ", bg='#ffb380', fg="#0000e6", font="Times 13 bold").place(x=10, y=190)
            ps = Label(slip, text=menu1.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=190)

            ap_city = Label(slip, text="City : ", bg='#ffb380', fg="#0000e6", font="Times 13 bold").place(x=10, y=220)
            pc = Label(slip, text=menu2.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=220)

            ap_place= Label(slip, text="Date : ", bg='#ffb380', fg="#0000e6", font="Times 13 bold").place(x=10, y=250)
            ppla = Label(slip, text=lab.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=250)

            ap_vac = Label(slip, text="Vaccine : ", bg='#ffb380', fg="#0000e6", font="Times 13 bold").place(x=10, y=290)
            pv = Label(slip, text=lk.get(), font="TIMES 13 bold", fg="#0000e6", bg="#ffb380").place(x=80, y=290)

def clear_text():
    v1.delete(0, END)
    v2.delete(0, END)
    v3.delete(0, END)
    v4.delete(0, END)
    v5.delete(0, END)


# conigure is used to change the bg color of whole window
root.configure(bg='#ffb380')
root.mainloop()

