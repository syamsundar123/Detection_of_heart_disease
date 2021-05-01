from tkinter import *  # Importing modules
from PIL import ImageTk, Image
from tkinter import messagebox


# ==================================================First Page================================================================
def landing_page():
    global Landingpage
    Landingpage = Tk()  # Creating a window
    Landingpage.configure(bg="#D79922")  # 45A29E
    Landingpage.title("Medication Of Heart Disease.")  # Window Title
    # Landingpage.iconbitmap("ap.ico")
    width = Landingpage.winfo_screenwidth()  # Geometry Of Window(Width and Height)
    height = Landingpage.winfo_screenheight()
    Landingpage.geometry(f'{width}x{height}')
    # ==============================================Canvas for Image==================================================================
    canvas = Canvas(Landingpage, width=900, height=380)
    image = ImageTk.PhotoImage(Image.open("healthy-life-banner.png"))
    canvas.create_image(448, 190, image=image)
    canvas.place(relx=0.20, rely=0.2)
    # ===============================================Upper Frame========================================================================
    frame = Frame(Landingpage, bg="#45A29E", height=150, width=1500, padx=0)
    frame.place(relx=0.01, rely=0.01)
    txt = """        "The most chronic heart disease is caused by having greediness in your heart. 
          Go for check ups regularly and learn how to swallow those lumpy pills of generousity.
            Be kind and be healthy." """
    Label(frame, bg="purple", fg="white", text=txt, height=3, width=81, font=('comic sans ms', '22')).place(relx=0.01,
                                                                                                            rely=0.1)

    # ===============================================Lower Frame=====================================================================
    lframe = Frame(Landingpage, bg="#45A29E", height=180, width=1500, padx=0)
    lframe.place(relx=0.01, rely=0.71)
    txt1 = "Welcome to the world of Medication Of Heart Disease. Click 'Start' and select your Symptoms to know your Disease."
    Label(lframe, bg="purple", fg="white", text=txt1, height=3, width=98, font=('comic sans ms', '18')).place(
        relx=0.007, rely=0.05)
    Button(lframe, text="Start", font=('comic sans ms', '18'), cursor="hand2", bg='green', fg='white',
           activebackground='green', command=lambda: Medication()).place(relx=0.45, rely=0.64)
    Landingpage.mainloop()


# ===================================================Symptoms Page==============================================================
def Medication():
    global win
    win = Toplevel(Landingpage)
    win.title("Medication Of Heart Disease")
    # win.iconbitmap("ap.ico")
    global width
    global height
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry(f'{width}x{height}')
    canvas = Canvas(win, width=width, height=height)
    image = ImageTk.PhotoImage(Image.open("Background_image.jpg"))
    canvas.create_image(0, 0, anchor="nw", image=image)
    canvas.place(relx=0, rely=0)
    # ===============================================Labels=====================================================================
    for i in range(0, len(Symptoms)):
        if (i > 19):
            i = i - 20
            Label(win, text=Symptoms[i + 20], font=('comic sans ms', '20'), bg="green", fg="white", anchor="w",
                  width=20).place(relx=0.69, rely=i * 0.1)
        elif (i > 9):
            i = i - 10
            Label(win, text=Symptoms[i + 10], font=('comic sans ms', '20'), bg="green", fg="white", anchor="w",
                  width=20).place(relx=0.34, rely=i * 0.1)

        else:
            Label(win, text=Symptoms[i], bg='green', fg='white', font=('comic sans ms', '20'), anchor="w",
                  width=20).place(relx=0, rely=i * 0.1)

    # =============================================DropDown Box==================================================================
    sev = [0, 1, 2, 3, 4, 5]
    variable = [0 for i in range(0, len(Symptoms))]
    for i in range(0, len(Symptoms)):
        variable[i] = IntVar()
        variable[i].set(0)

        d = OptionMenu(win, variable[i], *sev)
        d.config(bg="lightsalmon", activebackground="pink", anchor="w", relief="flat", font=('comic sans ms', '12'),
                 width=10, height=2, cursor="hand2")
        if (i > 19):
            i = i - 20
            d.place(relx='0.905', rely=i * 0.1)
        elif (i > 9):
            i = i - 10
            d.place(relx='0.555', rely=i * 0.1)
        else:
            d.place(relx='0.215', rely=i * 0.1)

    # ===================================================Logic===================================================================

    global getlist
    getlist = []

    def get():
        for i in range(0, len(variable)):
            if variable[i].get() > 0 and Symptoms[i] not in getlist:
                # print(Symptoms[i],"is:",variable[i].get())
                getlist.append(Symptoms[i])
        # print(getlist)
        if len(getlist) > 0:
            result_page()

        else:
            messagebox.showinfo("Warning", "Please Select your Symptoms...!")

    Button(win, text="SUBMIT", bg='saddlebrown', fg='black', activebackground="saddlebrown", cursor="hand2",
           font=('comic sans ms', '20'), anchor="center", width=20, command=lambda: get()).place(relx=0.72, rely=0.88)
    win.mainloop()


# ==================================================Result Page===================================================================

def result_page():
    global result
    result = Toplevel(win)
    result.title("Result Page")
    # result.iconbitmap("ap.ico")
    result.geometry(f'{width}x{height}')
    canvas = Canvas(result, width=width, height=height)
    image = ImageTk.PhotoImage(Image.open("Background_image.jpg"))
    canvas.create_image(0, 0, anchor="nw", image=image)
    canvas.pack()

    # ===================================================Logic=======================================================================
    Label(result, text="You Selected Below Symptoms:", bg='chocolate1', fg='white', font=('comic sans ms', '20'),
          anchor="w").place(relx=0.05, rely=0.04)
    for i in range(0, len(getlist)):
        if i > 9:
            i = i - 9
            Label(result, text=str(i + 9) + ")" + getlist[i], bg='green', fg='white', font=('comic sans ms', '20'),
                  anchor="w", width=25).place(relx=0.4, rely=i * 0.1)

        i = i + 1
        Label(result, text=str(i) + ")" + getlist[i - 1], bg='green', fg='white', font=('comic sans ms', '20'),
              anchor="w", width=25).place(relx=0.1, rely=i * 0.1)

    global count1, count2, count3, count4, count5, count6
    count1 = count2 = count3 = count4 = count5 = count6 = 0
    for i in getlist:
        if i in Coronary_Artery_Diseases:
            count1 += 1
        elif i in Myocardial_Infarction:
            count2 += 1
        elif i in Heart_Defects:
            count3 += 1
        elif i in Arythmia:
            count4 += 1
        elif i in Hypotension:
            count5 += 1
        elif i in Peripheral_Arterial_Disease:
            count6 += 1

    if count1 <= 3 and count2 <= 3 and count3 <= 3 and count4 <= 3 and count5 <= 3 and count6 <= 3:
        messagebox.showwarning("Warning", "InSufficient Data,Please Select Correct Symptoms...!")

        getlist.clear()
    if (count1 + count2 + count3 + count4 + count5 + count6) > 10:
        messagebox.showwarning("Warning", "Please Select Correct Symptoms...!")
        getlist.clear()

    lb1 = Label(result, bg='chocolate1', width=22, height=10, fg='white', font=('comic sans ms', '20'), anchor="w")
    lb1.place(relx=0.65, rely=0.14)
    if count1 > 3:
        Label(lb1, bg='pink', text="You are suffering from ", fg='black', width=22, font=('comic sans ms', '15')).place(
            relx=0.1, rely=0.2)
        Label(lb1, bg='pink', text="Coronary Artery Disease.", fg='black', font=('comic sans ms', '20', 'bold')).place(
            relx=0.01, rely=0.3)
    elif count2 > 3:
        Label(lb1, bg='pink', text="You are suffering from ", fg='black', width=22, font=('comic sans ms', '15')).place(
            relx=0.1, rely=0.2)
        Label(lb1, bg='pink', text="Myocardial Infarction", fg='black', font=('comic sans ms', '20', 'bold')).place(
            relx=0.08, rely=0.3)
    elif count3 > 3:
        Label(lb1, bg='pink', text="You are suffering from ", fg='black', width=22, font=('comic sans ms', '15')).place(
            relx=0.1, rely=0.2)
        Label(lb1, bg='pink', text="Heart Defects", fg='black', font=('comic sans ms', '20', 'bold')).place(relx=0.25,
                                                                                                            rely=0.3)
    elif count4 > 3:
        Label(lb1, bg='pink', text="You are suffering from ", fg='black', width=22, font=('comic sans ms', '15')).place(
            relx=0.1, rely=0.2)
        Label(lb1, bg='pink', text="Arythmia", fg='black', font=('comic sans ms', '20', 'bold')).place(relx=0.26,
                                                                                                       rely=0.3)
    elif count5 > 3:
        Label(lb1, bg='pink', text="You are suffering from ", fg='black', width=22, font=('comic sans ms', '15')).place(
            relx=0.1, rely=0.2)
        Label(lb1, bg='pink', text="Hypotension", fg='black', font=('comic sans ms', '20', 'bold')).place(relx=0.25,
                                                                                                          rely=0.3)
    elif count6 > 3:
        Label(lb1, bg='pink', text="You are suffering from ", fg='black', width=22, font=('comic sans ms', '15')).place(
            relx=0.1, rely=0.2)
        Label(lb1, bg='pink', text="Peripheral Arterial Disease", fg='black',
              font=('comic sans ms', '19', 'bold')).place(relx=0.02, rely=0.3)

    def destroy():
        result.destroy()
        win.destroy()
        Landingpage.destroy()

    Button(lb1, text="OK", fg="white", bg="red", activebackground="red", font=('comic sans ms', '20'),
           command=lambda: destroy()).place(relx=0.4, rely=0.6)
    Label(lb1, bg='Black', text="(Click OK to exit)", fg='white', font=('comic sans ms', '15')).place(relx=0.27,
                                                                                                      rely=0.8)
    result.mainloop()


# ======================================================Main=====================================================================

Heart_Diseases = ['Coronary Artery Diseases', 'Myocardial Infarction', 'Arythmia',
                  ' Heart Defects', ' Peipheral Heart Disease', 'Hypotension']

Symptoms = ['Shortness Of Breathing', 'Sweating', 'Weakness', 'Nausea', 'Dizziness', 'Palpitations',
            'Rapid Heartbeat', 'Tightness in the Chest', 'Couch', 'Anxiety', 'Fast Heart Rate',
            'Swelling Of Body Tissues',
            'Abnormal Heart Rhythms', 'A Bluish Tint On Skin', 'Tiring Quickly upon Exertion', 'Fluttering in Chest',
            'Racing HeartBeat', 'Chestpain', 'Fainting', 'Lightheadedness', 'Fatigue', 'Paleskin',
            'Weak and Rapid Pulse'
    , 'Lack Of Concentration', 'Hairloss on feet and legs', 'Leg Weakness', 'Lowerleg feelscold', 'Numbness in Legs',
            'Brittle toe Nails']

Coronary_Artery_Diseases = ['Shortness Of Breathing', 'Sweating', 'Weakness', 'Nausea', 'Dizziness', 'Palpitations',
                            'Rapid Heartbeat']
Myocardial_Infarction = ['Tightness in the Chest', 'Sweating', 'Couch', 'Nausea', 'Anxiety', 'Fast Heart Rate']
Heart_Defects = ['Swelling Of Body Tissues', 'Abnormal Heart Rhythms', 'A Bluish Tint On Skin',
                 'Tiring Quickly upon Exertion']
Arythmia = ['Fluttering in Chest', 'Racing HeartBeat', 'Chestpain', 'Sweating', 'Fainting', 'Anxiety']
Hypotension = ['Lightheadedness', 'Fainting', 'Nausea', 'Fatigue', 'Paleskin', 'Weak and Rapid Pulse',
               'Lack Of Concentration']
Peripheral_Arterial_Disease = ['Hairloss on feet and legs', 'Leg Weakness', 'Lowerleg feelscold', 'Numbness in Legs',
                               'Brittle toe Nails']

landing_page()