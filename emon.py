#sign up window
#to get details to create user account

from tkinter import ttk,PhotoImage
import tkinter as tk
import tkinter.messagebox as msg
import mysql.connector as s
import numpy as np
import matplotlib.pyplot as plt
mc=s.connect(host="localhost",user="root",passwd="1129",database="emon_db")
cr=mc.cursor()
global AADHAR

#readings page
def statistics():
    top.destroy()
    def warningunitconsumeddomest(week3sum):
        if(week3sum>=80  and week3sum<100):
              msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 2.25 rupees for every unit".format(100-week3sum))
        if(week3sum>=170 and week3sum<200):
              msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 4.5 rupees for every unit".format(200-week3sum))
        if(week3sum>=360 and week3sum<500):
              msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 6 rupees for every unit".format(500-week3sum))
        

    def warningunitconsumedcomm(week3sum1):
        if(week3sum1>=80 and week3sum1<100):
               msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 4.5 rupees for every unit".format(100-week3sum1))
        if(week3sum1>=370 and week3sum1<400):
               msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 6 rupees for every unit".format(400-week3sum1))
        if(week3sum1>=460 and week3sum1<500):
               msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 8 rupees for every unit".format(500-week3sum1))
        if(week3sum1>=560 and week3sum1<600):
               msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 9 rupees for every unit".format(600-week3sum1))
        if(week3sum1>=760 and week3sum1<800):
               msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 10 rupees for every unit".format(800-week3sum1))
        if(week3sum1>=950 and week3sum1<1000):
               msg.showinfo("warning","You have only {} more units to consume for this month,else you should pay 11 rupees for every unit".format(1000-week3sum1))
        if(week3sum1>=1000):
               msg.showinfo("warning","You have exceeded 1000 units,your amount is rupees 11 for each unit")

    #week-1
    q1="select w1 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q1)
    w1=cr.fetchone()[0]
    #week-2
    q2="select w2 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q2)
    w2=cr.fetchone()[0]
    #week-3
    q3="select w3 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q3)
    w3=cr.fetchone()[0]
    #week-4
    q4="select w4 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q4)
    w4=cr.fetchone()[0]
    #week-5
    q5="select w5 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q5)
    w5=cr.fetchone()[0]
    #week-6
    q6="select w6 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q6)
    w6=cr.fetchone()[0]
    #week-7
    q7="select w7 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q7)
    w7=cr.fetchone()[0]
    #week-8
    q8="select w8 from weekly where aadhar={}".format(AADHAR)
    cr.execute(q8)
    w8=cr.fetchone()[0]
    query="select choice from threshold where aadhar={}".format(AADHAR)
    cr.execute(query)
    ch=cr.fetchone()[0]
    if(ch==1):
        warningunitconsumeddomest(w5+w6+w7)  
    elif(ch==2):
        warningunitconsumedcomm(w5+w6+w7)

    #plot code
    data1 = [w1,w2,w3,w4]
    data2=[w5,w6,w7,0]
    X = np.arange(4)
    
    plt.bar(X + 0.00, data1, color = 'b', width = 0.25,label="March")
    plt.bar(X + 0.25, data2, color = 'r', width = 0.25,label="April")
    plt.legend(loc='upper left')
    plt.xticks(X,["week1","week2","week3","week4"])
    plt.title("Weekly Analysis of Power consumption")
    plt.xlabel("Weeks")
    plt.ylabel("Power Consumption (in units)")
    plt.show()

def reading_enter():
    
    def retrieve_input():
        reading1=int(txtr1.get("1.0","end-1c"))
        reading2=int(txtr2.get("1.0","end-1c"))
        save_percent=int(Y.get())
        avg=(reading1+reading2)/2
        maxlim=avg-(save_percent/100)*avg
        tk.Label(window,text="You have to consume a maximum of {}".format(maxlim),width=60,font="CALIBRI 15",relief='raised').place(y=650,x=500)
        choice  = radio.get()
        cr.execute("insert into threshold values({},{},{},{},{},{},{})".format(AADHAR,reading1,reading2,avg,save_percent,maxlim,choice))
        mc.commit()

    window = tk.Tk()
    window.title("Getting details of power consumption")
    window.state('zoomed')
    img2=PhotoImage(master=window,file="image5.png")
    tk.Label(window,image=img2).place(y=50,x=150)

    tk.Label(window,text="POWER CONSUMPTION TYPE",width=40,font="CALIBRI 15",relief='raised').place(y=100,x=200)


    def selection():
       selected = "You have selected " + str(radio.get())
       
    radio = tk.IntVar()
    r1 = tk.Radiobutton(window, text="Domestic", variable=radio, value=1, command=selection).place(y=100,x=800)
    r2 = tk.Radiobutton(window, text="Commercial", variable=radio, value=2, command=selection).place(y=130,x=800)

    tk.Label(window,text="POWER CONSUMPTION OF LAST 4 MONTHS",width=60,font="CALIBRI 15",relief='raised').place(y=50,x=500)
    tk.Label(window,text="Reading 1:", width=40,font="CALIBRI 15",relief='raised').place(y=200,x=200)
    tk.Label(window,text="Reading 2:", width=40,font="CALIBRI 15",relief='raised').place(y=300,x=200)

    txtr1= tk.Text(window,width=40,height=1,font="CALIBRI 15",relief='raised')
    txtr1.place(y=200,x=800)
    txtr2 = tk.Text(window,width=40,height=1,font="CALIBRI 15",relief='raised')
    txtr2.place(y=300,x=800)

    tk.Label(window,text="How much power do you want to save:(in %)",width=40,font="CALIBRI 15",relief='raised').place(y=400,x=200)

    Y = ttk.Combobox(window,font="CALIBRI 15")
    Y['values']=('5','10','15')
    Y.place(y=400,x=800)
    Y.current(0)

    btn = tk.Button(window,text="SUBMIT",height=5,width=20,command=retrieve_input).place(y=500,x=700)
    window.mainloop()
#user login page
def loginp():                 #login
    rootp.destroy()
    global top
    top = tk.Tk()
    top.state('zoomed')
    top.title("Login")
    top.configure(bg='light sea green')
    img1=PhotoImage(master=top,file="image3.png")
    tk.Label(top,image=img1).place(y=50,x=150)
    def submit():                 #checking whether login details are correct

        u=u_entry.get()
        passw=passw_entry.get() 
        
        query="select * from user_details where user_id='{}' and pwd='{}' ".format(u,passw)
        cr.execute(query)
        data=cr.fetchone()

        if data!=None:
            display_label=tk.Button(top,text="Welcome to EMON\nClick here to proceed>>",height=3,width=25,bg='PaleTurquoise1',font=('Comic Sans MS',15),command=statistics)
            display_label.place(y=500,x=800)
            global AADHAR
            AADHAR=data[3]
            
        else:
            msg.showwarning("showwarning","User ID or Password is Invalid\nSORRY. TRY AGAIN!!!")

        
        
        
    u_label=tk.Label(top,text="USER ID (EMAIL)",bg='snow',font=('Comic Sans MS',25))
    u_label.place(y=200,x=400)
    u_entry=tk.Entry(top,font=('Comic Sans MS',25))
    u_entry.place(y=200,x=750)
    
    passw_label = tk.Label(top,text = 'Password',bg='snow',font=('Comic Sans MS',25))
    passw_label.place(y=300,x=400)
    passw_entry=tk.Entry(top, font = ('Comic Sans MS',25),show="*")
    passw_entry.place(y=300,x=750)
    sub_img = PhotoImage(master=top, file=r"D:\#VIT\emon\submit.png")
    sub = tk.Button(top,text="SUBMIT",height=3,width=15,bg='PaleTurquoise1',font=('Comic Sans MS',15),command=submit)
    sub.place(y=500, x=500)
    top.mainloop()

#user registration window
def sign_up():
    signp = tk.Tk()
    signp.title("User Registration")
    signp.state('zoomed')
    signp.configure(bg='DeepSkyBlue4')
    img3=PhotoImage(master=signp,file="image4.png")
    tk.Label(signp,image=img3).place(y=50,x=150)
    
    #label boxes
    tk.Label(signp,text="User - Mail ID",width=15,font="CALIBRI 15",bg='green yellow',relief='raised').place(y=100,x=200)
    tk.Label(signp,text="User Name",width=15,font="CALIBRI 15",bg='green yellow',relief='raised').place(y=200,x=200)
    tk.Label(signp,text="Password",width=15,font="CALIBRI 15",bg='green yellow',relief='raised').place(y=300,x=200)
    tk.Label(signp,text="Aadhar Number",width=15,font="CALIBRI 15",bg='green yellow',relief='raised').place(y=400,x=200)
    #text boxes
    txtUserID= tk.Text(signp,width=45,height=1,font="CALIBRI 15",relief='raised')
    txtUserID.place(y=100,x=400)
    txtUname= tk.Text(signp,width=45,height=1,font="CALIBRI 15",relief='raised')
    txtUname.place(y=200,x=400)
    txtpwd=tk.Entry(signp,show='*',width=45,font="CALIBRI 15",relief='raised')
    txtpwd.place(y=300,x=400)
    txtAadhar= tk.Text(signp,width=45,height=1,font="CALIBRI 15",relief='raised')
    txtAadhar.place(y=400,x=400)

    def save():
        
        user_id=txtUserID.get(1.0,"end-1c")
        uname=txtUname.get(1.0,'end-1c')
        pwd=txtpwd.get()
        aadhar=txtAadhar.get(1.0,'end-1c')
        global AADHAR
        AADHAR=aadhar
        q="select aadhar from user_details"
        cr.execute(q)
        all_records=cr.fetchall()
        flag=True
        if "" not in [user_id,uname,pwd,aadhar]:
            try:
                cr.execute("insert into user_details values('{}','{}','{}',{})".format(user_id,uname,pwd,int(aadhar)))
                mc.commit()
            except:
                flag=False
                mc.rollback()
            if flag==True:
                reading_enter()
            else:
                msg.showwarning("Warning","User ID already exists")
                signp.destroy()       
                    
        else:
            msg.showwarning("showwarning","All fields are compulsory")
        
        
        
    savebutton=PhotoImage(master=signp,file="savebtn.png")
    btn = ttk.Button(signp,image=savebutton,command=save).place(y=500,x=350)
    signp.mainloop()
    
rootp=tk.Tk()
rootp.title("Welcome to EMON")
rootp.state("zoomed")
im=PhotoImage(master=rootp,file="mainp.png")
tk.Label(rootp,image=im).pack()
sign=PhotoImage(master=rootp,file="signbtn.png")
login=PhotoImage(master=rootp,file="loginbtn.png")
B1=ttk.Button(rootp,image=sign,command=sign_up).place(x=300,y=550)
B2=ttk.Button(rootp,image=login,command=loginp).place(x=500,y=550)
rootp.mainloop()
mc.close()



