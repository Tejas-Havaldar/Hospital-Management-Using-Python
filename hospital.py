from logging.config import valid_ident
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import mysql

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Variables to store the information

        self.nameOfTablets = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.numberOfTablets = StringVar()
        self.lot = StringVar()
        self.issueDate = StringVar()
        self.expiryDate = StringVar()
        self.dailyDose = StringVar()
        self.sideEffects = StringVar()
        self.furtherInformation = StringVar()
        self.bloodPreesure = StringVar()
        self.drivingUsingMachine = StringVar()
        self.howToStore = StringVar()
        self.howToUseMedication = StringVar()
        self.patientId = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.dateOfBirth = StringVar()
        self.patientAddress = StringVar()

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("vardhana",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # Frame for Patient info and prescription

        dataframe = Frame(self.root,bd=20,relief=RIDGE) # Main data frame
        dataframe.place(x=0,y=130,width=1530,height=400)

        dataframe_left = LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("vardhana",12,"bold"),text="Patient Information") # Main Left Data Frame
        dataframe_left.place(x=0,y=5,width=980,height=350)

        # Entry Field in Left Dataframe

        label_name_tablet = Label(dataframe_left,text="Name of Tablet",font=("vardhana",12,"normal"),padx=5,pady=6) # First Entry Field LEFT
        label_name_tablet.grid(row=0,column=0,sticky=W)
        com_name_tablet = ttk.Combobox(dataframe_left,textvariable=self.nameOfTablets, font=("vardhana",12,"normal"),width=33)
        com_name_tablet["values"] = ("Asprin","ZinCold","Pfizer","Adderal","Heroin","Crystal Meth","Ecstasy","Cocaine")
        com_name_tablet.grid(row=0,column=1)

        label_name_ref = Label(dataframe_left,text="Reference Number",font=("vardhana",12,"normal"),padx=5,pady=6) # Second Entry Field
        label_name_ref.grid(row=1,column=0,sticky=W)
        txt_ref = Entry(dataframe_left,textvariable=self.ref, font=("vardhana",12,"normal"),width=35)
        txt_ref.grid(row=1,column=1)

        label_dose = Label(dataframe_left,text="Dose",font=("vardhana",12,"normal"),padx=5,pady=6) # Third Entry Field
        label_dose.grid(row=2,column=0,sticky=W)
        txt_dose = Entry(dataframe_left,textvariable=self.dose, font=("vardhana",12,"normal"),width=35)
        txt_dose.grid(row=2,column=1)

        label_no_of_tablet = Label(dataframe_left,text="No of tablets",font=("vardhana",12,"normal"),padx=5,pady=6) # Fourth Entry Field
        label_no_of_tablet.grid(row=3,column=0,sticky=W)
        txt_no_of_tablet = Entry(dataframe_left,textvariable=self.numberOfTablets, font=("vardhana",12,"normal"),width=35)
        txt_no_of_tablet.grid(row=3,column=1)

        label_lot = Label(dataframe_left,text="Lot",font=("vardhana",12,"normal"),padx=5,pady=6) # Fifth Entry Field
        label_lot.grid(row=4,column=0,sticky=W)
        txt_lot = Entry(dataframe_left,textvariable=self.lot, font=("vardhana",12,"normal"),width=35)
        txt_lot.grid(row=4,column=1)

        label_issue_date = Label(dataframe_left,text="Issue Date",font=("vardhana",12,"normal"),padx=5,pady=6) # Sixth Entry Field
        label_issue_date.grid(row=5,column=0,sticky=W)
        txt_issue_date = Entry(dataframe_left,textvariable=self.issueDate, font=("vardhana",12,"normal"),width=35)
        txt_issue_date.grid(row=5,column=1)

        label_exp_date = Label(dataframe_left,text="Expiry Date",font=("vardhana",12,"normal"),padx=5,pady=6) # Seventh Entry Field
        label_exp_date.grid(row=6,column=0,sticky=W)
        txt_exp_date = Entry(dataframe_left,textvariable=self.expiryDate, font=("vardhana",12,"normal"),width=35)
        txt_exp_date.grid(row=6,column=1)

        label_daily_dose = Label(dataframe_left,text="Daily Dose",font=("vardhana",12,"normal"),padx=5,pady=6) # Eighth Entry Field
        label_daily_dose.grid(row=7,column=0,sticky=W)
        txt_daily_dose = Entry(dataframe_left,textvariable=self.dailyDose, font=("vardhana",12,"normal"),width=35)
        txt_daily_dose.grid(row=7,column=1)

        label_side_effect = Label(dataframe_left,text="Side Effects",font=("vardhana",12,"normal"),padx=5,pady=6) # Ninth Entry Field
        label_side_effect.grid(row=8,column=0,sticky=W)
        txt_side_effect = Entry(dataframe_left,textvariable=self.sideEffects, font=("vardhana",12,"normal"),width=35)
        txt_side_effect.grid(row=8,column=1)

        label_further_info = Label(dataframe_left,text="Further Information",font=("vardhana",12,"normal"),padx=5,pady=6) # First Entry Field RIGHT
        label_further_info.grid(row=0,column=2,sticky=W)
        txt_further_info = Entry(dataframe_left,textvariable=self.furtherInformation, font=("vardhana",12,"normal"),width=35)
        txt_further_info.grid(row=0,column=3)

        label_blood_p = Label(dataframe_left,text="Blood Pressure",font=("vardhana",12,"normal"),padx=5,pady=6) # Second Entry Field
        label_blood_p .grid(row=1,column=2,sticky=W)
        txt_blood_p  = Entry(dataframe_left,textvariable=self.bloodPreesure, font=("vardhana",12,"normal"),width=35)
        txt_blood_p .grid(row=1,column=3)

        label_storage_adv = Label(dataframe_left,text="Storage Advice",font=("vardhana",12,"normal"),padx=5,pady=6) # Third Entry Field
        label_storage_adv.grid(row=2,column=2,sticky=W)
        txt_storage_adv = Entry(dataframe_left,textvariable=self.howToStore, font=("vardhana",12,"normal"),width=35)
        txt_storage_adv.grid(row=2,column=3)

        label_medication = Label(dataframe_left,text="Medication",font=("vardhana",12,"normal"),padx=5,pady=6) # Fourth Entry Field
        label_medication.grid(row=3,column=2,sticky=W)
        txt_medication = Entry(dataframe_left,textvariable=self.howToUseMedication, font=("vardhana",12,"normal"),width=35)
        txt_medication.grid(row=3,column=3)

        label_patient_id = Label(dataframe_left,text="Patient ID",font=("vardhana",12,"normal"),padx=5,pady=6) # Fifth Entry Field
        label_patient_id.grid(row=4,column=2,sticky=W)
        txt_patient_id = Entry(dataframe_left,textvariable=self.patientId, font=("vardhana",12,"normal"),width=35)
        txt_patient_id.grid(row=4,column=3)

        label_nhs_no = Label(dataframe_left,text="NHS Number",font=("vardhana",12,"normal"),padx=5,pady=6) # Sixth Entry Field
        label_nhs_no .grid(row=5,column=2,sticky=W)
        txt_nhs_no  = Entry(dataframe_left,textvariable=self.nhsNumber, font=("vardhana",12,"normal"),width=35)
        txt_nhs_no .grid(row=5,column=3)

        label_patient_name = Label(dataframe_left,text="Patient Name",font=("vardhana",12,"normal"),padx=5,pady=6) # Seventh Entry Field
        label_patient_name.grid(row=6,column=2,sticky=W)
        txt_patient_name = Entry(dataframe_left,textvariable=self.patientName, font=("vardhana",12,"normal"),width=35)
        txt_patient_name.grid(row=6,column=3)

        label_date_of_birth = Label(dataframe_left,text="Date Of Birth",font=("vardhana",12,"normal"),padx=5,pady=6) # Eighth Entry Field
        label_date_of_birth.grid(row=7,column=2,sticky=W)
        txt_date_of_birth = Entry(dataframe_left,textvariable=self.dateOfBirth, font=("vardhana",12,"normal"),width=35)
        txt_date_of_birth.grid(row=7,column=3)

        label_patient_add = Label(dataframe_left,text="Patient Address",font=("vardhana",12,"normal"),padx=2,pady=6) # Ninth Entry Field
        label_patient_add.grid(row=8,column=2,sticky=W)
        txt_patient_add = Entry(dataframe_left,textvariable=self.patientAddress, font=("vardhana",12,"normal"),width=35)
        txt_patient_add.grid(row=8,column=3)

        ##
        dataframe_right = LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("vardhana",12,"bold"),text="Prescription") # Main Right Data Frame
        dataframe_right.place(x=990,y=5,width=460,height=350)

        self.txt_prescription = Text(dataframe_right,font=("vardhana",12,"bold"),width=45,height=16,padx=5,pady=6) # To show data from left frame
        self.txt_prescription.grid(row=0,column=0)
        ##

        # Frame for buttons

        buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        buttonframe.place(x=0,y=530,width=1530,height=70)

        btn_prescription = Button(buttonframe,command=self.i_prescription, text="Prescription",bg="green",fg="black",font=("vardhana",12,"bold"),width=23,padx=5,pady=6)
        btn_prescription.grid(row=0,column=0)

        btn_prescription_data = Button(buttonframe,command=self.i_prescription_data ,text="Prescription Data",bg="green",fg="black",font=("vardhana",12,"bold"),width=23,padx=5,pady=6)
        btn_prescription_data.grid(row=0,column=1)

        btn_update = Button(buttonframe,command=self.update_data, text="Update",bg="green",fg="black",font=("vardhana",12,"bold"),width=23,padx=5,pady=6)
        btn_update.grid(row=0,column=2)

        btn_delete = Button(buttonframe,command=self.delete_data, text="Delete",bg="green",fg="black",font=("vardhana",12,"bold"),width=23,padx=5,pady=6)
        btn_delete.grid(row=0,column=3)

        btn_clear = Button(buttonframe,command=self.clear_data, text="Clear",bg="green",fg="black",font=("vardhana",12,"bold"),width=23,padx=5,pady=6)
        btn_clear.grid(row=0,column=4)

        btn_exit = Button(buttonframe,command=self.exit_window, text="Exit",bg="green",fg="black",font=("vardhana",12,"bold"),width=23,padx=5,pady=6)
        btn_exit.grid(row=0,column=5)

        ##
        # Frame for details

        detail_frame = Frame(self.root,bd=20,relief=RIDGE) # Main Details Frame
        detail_frame.place(x=0,y=600,width=1530,height=190)

        # To make scroll bars
        scroll_x = ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_frame,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(detail_frame,column = ("name_of_tablet","ref","dose","no_of_tablet","lot","issue_date",
                                                            "expiry_date","daily_dose","storage","nhs_number","p_name","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("name_of_tablet", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("no_of_tablet", text="Number of tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issue_date", text="Issue Date")
        self.hospital_table.heading("expiry_date", text="Expiry Date")
        self.hospital_table.heading("daily_dose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhs_number", text="NHS Number")
        self.hospital_table.heading("p_name", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.column("name_of_tablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issue_date",width=100)
        self.hospital_table.column("expiry_date",width=100)
        self.hospital_table.column("daily_dose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhs_number",width=100)
        self.hospital_table.column("p_name",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
 
    # Functionality Declaration
    # Working on buttons

    def i_prescription_data(self):
        if self.nameOfTablets == "" or self.ref == "":
            messagebox.showerror("Error","All field are required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="toor",database="Hospital_Management")      
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                self.nameOfTablets.get(),
                self.ref.get(),
                self.dose.get(),
                self.numberOfTablets.get(),
                self.lot.get(),
                self.issueDate.get(),
                self.expiryDate.get(),
                self.dailyDose.get(),
                self.howToStore.get(),
                self.nhsNumber.get(),
                self.patientName.get(),
                self.dateOfBirth.get(),
                self.patientAddress.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success","Information has been added to the database")
        
    def update_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="toor",database="Hospital_Management")      
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set name_of_tablet=%s,dose=%s,no_of_tablet=%s,lot=%s,issue_date=%s,expiry_date=%s,daily_dose=%s,storage=%s,nhs_number=%s,p_name=%s,dob=%s,address=%s where ref=%s",
            (
                self.nameOfTablets.get(),
                self.dose.get(),
                self.numberOfTablets.get(),
                self.lot.get(),
                self.issueDate.get(),
                self.expiryDate.get(),
                self.dailyDose.get(),
                self.howToStore.get(),
                self.nhsNumber.get(),
                self.patientName.get(),
                self.dateOfBirth.get(),
                self.patientAddress.get(),
                self.ref.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Update","Information has been updated")


    def i_prescription(self):
        self.txt_prescription.insert(END,"Name of the Tablet:\t\t\t" + self.nameOfTablets.get() + "\n")
        self.txt_prescription.insert(END,"Reference Number:\t\t\t" + self.ref.get() + "\n")
        self.txt_prescription.insert(END,"Dose:\t\t\t" + self.dose.get() + "\n")
        self.txt_prescription.insert(END,"No. of Tablets:\t\t\t" + self.numberOfTablets.get() + "\n")
        self.txt_prescription.insert(END,"Lot:\t\t\t" + self.lot.get() + "\n")
        self.txt_prescription.insert(END,"Issue Date:\t\t\t" + self.issueDate.get() + "\n")
        self.txt_prescription.insert(END,"Expiry Date:\t\t\t" + self.expiryDate.get() + "\n")
        self.txt_prescription.insert(END,"Daily Dose:\t\t\t" + self.dailyDose.get() + "\n")
        self.txt_prescription.insert(END,"Side Effects:\t\t\t" + self.sideEffects.get() + "\n")
        self.txt_prescription.insert(END,"Further Information:\t\t\t" + self.furtherInformation.get() + "\n")
        self.txt_prescription.insert(END,"Blood Pressure:\t\t\t" + self.bloodPreesure.get() + "\n")
        self.txt_prescription.insert(END,"Storage Advice:\t\t\t" + self.howToStore.get() + "\n")
        self.txt_prescription.insert(END,"Medication:\t\t\t" + self.howToUseMedication.get() + "\n")
        self.txt_prescription.insert(END,"Patient ID:\t\t\t" + self.patientId.get() + "\n")
        self.txt_prescription.insert(END,"NHS Number:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txt_prescription.insert(END,"Patient Name:\t\t\t" + self.patientName.get() + "\n")
        self.txt_prescription.insert(END,"Date Of Birth:\t\t\t" + self.dateOfBirth.get() + "\n")
        self.txt_prescription.insert(END,"Patient Address:\t\t\t" + self.patientAddress.get() + "\n")

    def delete_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="toor",database="Hospital_Management")      
        my_cursor = conn.cursor()
        query = "delete from hospital where ref=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Delete","Patient has been deleted succesfully")

    def clear_data(self):
        self.nameOfTablets.set(""),
        self.ref.set(""),
        self.dose.set(""),
        self.numberOfTablets.set(""),
        self.lot.set(""),
        self.issueDate.set(""),
        self.expiryDate.set(""),
        self.dailyDose.set(""),
        self.sideEffects.set(""),
        self.furtherInformation.set(""),
        self.bloodPreesure.set(""),
        self.howToStore.set(""),
        self.howToUseMedication.set(""),
        self.patientId.set(""),
        self.nhsNumber.set(""),
        self.patientName.set(""),
        self.dateOfBirth.set(""),
        self.patientAddress.set("") 
        self.txt_prescription.delete("1.0",END)

    def exit_window(self):
        exit_win = messagebox.askyesno("Hospital Management System","Confirm if you want to exit")
        if exit_win>0:
            root.destroy()
            return
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="toor",database="Hospital_Management")      
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"] 
        self.nameOfTablets.set(row[0]),
        self.ref.set(row[1]),
        self.dose.set(row[2]),
        self.numberOfTablets.set(row[3]),
        self.lot.set(row[4]),
        self.issueDate.set(row[5]),
        self.expiryDate.set(row[6]),
        self.dailyDose.set(row[7]),
        self.howToStore.set(row[8]),
        self.nhsNumber.set(row[9]),
        self.patientName.set(row[10]),
        self.dateOfBirth.set(row[11]),
        self.patientAddress.set(row[12])        


root = Tk()
ob = Hospital(root)
root.mainloop()