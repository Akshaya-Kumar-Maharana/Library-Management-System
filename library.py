from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import cv2 
import tkinter

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")

        # **************************************Variable************************************** #
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.zip_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()




        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg = "green", bd=20, relief=RIDGE, font=("time new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1270, height = 330)
        # **************************************Data Frame Left************************************** #
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg = "green", bd=10, relief=RIDGE, font=("time new roman", 14, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y = 5, width=780, height=296)

        lblMember = Label(DataFrameLeft, bg="powder blue",text="Member Type", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable= self.member_var, font=("time new roman", 11, "bold"), width = 28, state="readonly")
        comMember["value"] = ("Admin Staff", "Professor", "Student")
        comMember.grid(row=0, column=1, sticky=W)

        lblPRN_Number = Label(DataFrameLeft, bg="powder blue", text="PRN Number", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblPRN_Number.grid(row=1, column=0, sticky=W)

        txtPRN_Number = Entry(DataFrameLeft, textvariable=self.prn_var,font=("time new roman", 11, "bold"), width = 30)
        txtPRN_Number.grid(row = 1, column = 1, sticky=W)

        lblTitle = Label(DataFrameLeft, bg="powder blue", text="ID Number", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblTitle.grid(row=2, column=0, sticky=W)

        txtTitle = Entry(DataFrameLeft, textvariable=self.id_var, font=("time new roman", 11, "bold"), width = 30)
        txtTitle.grid(row = 2, column = 1, sticky=W)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblFirstName.grid(row=3, column=0, sticky=W)

        txtFirstName = Entry(DataFrameLeft, textvariable=self.fname_var, font=("time new roman", 11, "bold"), width = 30)
        txtFirstName.grid(row = 3, column = 1, sticky=W)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblLastName.grid(row=4, column=0, sticky=W)

        txtLastName = Entry(DataFrameLeft, textvariable=self.lname_var, font=("time new roman", 11, "bold"), width = 30)
        txtLastName.grid(row = 4, column = 1, sticky=W)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblAddress1.grid(row=5, column=0, sticky=W)

        txtAddress1 = Entry(DataFrameLeft, textvariable=self.address1_var, font=("time new roman", 11, "bold"), width = 30)
        txtAddress1.grid(row = 5, column = 1, sticky=W)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address 2", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblAddress2.grid(row=6, column=0, sticky=W)

        txtAddress2 = Entry(DataFrameLeft, textvariable=self.address2_var, font=("time new roman", 11, "bold"), width = 30)
        txtAddress2.grid(row = 6, column = 1, sticky=W)

        lblZip = Label(DataFrameLeft, bg="powder blue", text="ZIP Code", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblZip.grid(row=7, column=0, sticky=W)

        txtZip = Entry(DataFrameLeft, textvariable=self.zip_var, font=("time new roman", 11, "bold"), width = 30)
        txtZip.grid(row = 7, column = 1, sticky=W)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile Number", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblMobile.grid(row=8, column=0, sticky=W)

        txtMobile = Entry(DataFrameLeft, textvariable=self.mobile_var, font=("time new roman", 11, "bold"), width = 30)
        txtMobile.grid(row = 8, column = 1, sticky=W)

        lblBookID = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblBookID.grid(row=0, column=2, sticky=W)

        txtBookID = Entry(DataFrameLeft, textvariable=self.bookid_var, font=("time new roman", 11, "bold"), width = 30)
        txtBookID.grid(row = 0, column = 3, sticky=W)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblBookTitle.grid(row=1, column=2, sticky=W)

        txtBookTitle = Entry(DataFrameLeft, textvariable=self.booktitle_var, font=("time new roman", 11, "bold"), width = 30)
        txtBookTitle.grid(row = 1, column = 3, sticky=W)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author's Name", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblAuthor.grid(row=2, column=2, sticky=W)

        txtAuthor = Entry(DataFrameLeft, textvariable=self.author_var, font=("time new roman", 11, "bold"), width = 30)
        txtAuthor.grid(row = 2, column = 3, sticky=W)

        lblDateBorrow = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblDateBorrow.grid(row=3, column=2, sticky=W)

        txtDateBorrow = Entry(DataFrameLeft, textvariable=self.dateborrowed_var,font=("time new roman", 11, "bold"), width = 30)
        txtDateBorrow.grid(row = 3, column = 3, sticky=W)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblDateDue.grid(row=4, column=2, sticky=W)

        txtDateDue = Entry(DataFrameLeft, textvariable=self.datedue_var, font=("time new roman", 11, "bold"), width = 30)
        txtDateDue.grid(row = 4, column = 3, sticky=W)

        lblDays = Label(DataFrameLeft, bg="powder blue", text="Days on Book", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblDays.grid(row=5, column=2, sticky=W)

        txtDays = Entry(DataFrameLeft, textvariable=self.daysonbook_var, font=("time new roman", 11, "bold"), width = 30)
        txtDays.grid(row = 5, column = 3, sticky=W)

        lblFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblFine.grid(row=6, column=2, sticky=W)

        txtFine = Entry(DataFrameLeft, textvariable=self.latereturnfine_var,font=("time new roman", 11, "bold"), width = 30)
        txtFine.grid(row = 6, column = 3, sticky=W)

        lblDue = Label(DataFrameLeft, bg="powder blue", text="Date over Due", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblDue.grid(row=7, column=2, sticky=W)

        txtDue = Entry(DataFrameLeft, textvariable=self.dateoverdue_var, font=("time new roman", 11, "bold"), width = 30)
        txtDue.grid(row = 7, column = 3, sticky=W)

        lblPrice = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("time new roman", 11, "bold"), padx=2,pady=3)
        lblPrice.grid(row=8, column=2, sticky=W)

        txtPrice = Entry(DataFrameLeft, textvariable=self.finalprice_var, font=("time new roman", 11, "bold"), width = 30)
        txtPrice.grid(row = 8, column = 3, sticky=W)

        # **************************************Data Frame Right************************************** #
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg = "green", bd=10, relief=RIDGE, font=("time new roman", 14, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=790, y = 5, width=420, height=296)

        self.textBox = Text(DataFrameRight, font=("time new roman", 9, "bold"), width=36, height = 16, padx = 2, pady = 3)
        self.textBox.grid(row = 0, column = 2, sticky = W)

        listScroll = Scrollbar(DataFrameRight)
        listScroll.grid(row = 0, column = 1, sticky="ns")
        listBooks = ["Alchemist", "Fault in Our Stars", "Introduction to Thermodynamics", "Ikigai", "My Journey"]

        def SelectBook(event=""):
            selected_index = listBox.curselection()[0]
            value = str(listBox.get(selected_index))
            # value = str(listBox.get(listBox.curselection))
            x = value
            if (x == "Alchemist"):
                self.bookid_var.set("BKID001")
                self.booktitle_var.set("Alchemist")
                self.author_var.set("Paulo Coelho")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d2 + d1 

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs 450")

            elif (x == "Fault in Our Stars"):
                self.bookid_var.set("BKID002")
                self.booktitle_var.set("Fault in Our Stars")
                self.author_var.set("John Green")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d2 + d1 

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs 450")

            elif (x == "Introduction to Thermodynamics"):
                self.bookid_var.set("BKID003")
                self.booktitle_var.set("Introduction to Thermodynamics")
                self.author_var.set("PB K Rao")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d2 + d1 

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs 450")
            
            elif (x == "Ikigai"):
                self.bookid_var.set("BKID004")
                self.booktitle_var.set("Ikigai")
                self.author_var.set("NA")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d2 + d1 

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs 450")

            elif (x == "My Journey"):
                self.bookid_var.set("BKID005")
                self.booktitle_var.set("My Journey")
                self.author_var.set("Akshaya")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d2 + d1 

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs 450")

        listBox = Listbox(DataFrameRight, font=("time new roman", 9, "bold"), width = 15, height = 15)
        listBox.grid(row =0, column = 0, padx = 2)
        listBox.bind("<<ListboxSelect>>", SelectBook)

        listScroll.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # **************************************Buttons************************************** #
        frame_button = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg="powder blue")
        frame_button.place(x=0, y=460, width=1270, height = 50)

        btnAddData = Button(frame_button, command=self.add_data, text = "Add Data", font=("time new roman", 10, "bold"), width = 24, bg= 'blue', fg = "white")
        btnAddData.grid(row = 0, column=0)

        btnAddData = Button(frame_button, command=self.showData, text = "Show Data", font=("time new roman", 10, "bold"), width = 24, bg= 'blue', fg = "white")
        btnAddData.grid(row = 0, column=1)

        btnAddData = Button(frame_button, command=self.update,text = "Update", font=("time new roman", 10, "bold"), width = 24, bg= 'blue', fg = "white")
        btnAddData.grid(row = 0, column=2)

        btnAddData = Button(frame_button, command = self.delete, text = "Delete", font=("time new roman", 10, "bold"), width = 24, bg= 'blue', fg = "white")
        btnAddData.grid(row = 0, column=3)

        btnAddData = Button(frame_button, command=self.reset, text = "Reset", font=("time new roman", 10, "bold"), width = 24, bg= 'blue', fg = "white")
        btnAddData.grid(row = 0, column=4)

        btnAddData = Button(frame_button, command=self.iexit, text = "Exit", font=("time new roman", 10, "bold"), width = 24, bg= 'blue', fg = "white")
        btnAddData.grid(row = 0, column=5)

        # **************************************Information************************************** #
        frame_database = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg="powder blue")
        frame_database.place(x=0, y=510, width=1270, height = 175)

        Table_frame = Frame(frame_database, bd=6, relief = RIDGE, bg = "powder blue")
        Table_frame.place(x = 0, y = 2, width = 1203, height =148)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, columns=["Member Type", "PRN no", "ID no", "First Name", "Last Name", "Address 1", "Address 2", "ZIP", "Mobile no", "Book ID", "Book Title", "Author's Name", "Date Borrowed", "Date Due", "Days on Book", "Late Return Fine", "Date over Due", "Actual Price"], xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member Type",text="Member Type")
        self.library_table.heading("PRN no",text="PRN no")
        self.library_table.heading("ID no",text="ID no")
        self.library_table.heading("First Name",text="First Name")
        self.library_table.heading("Last Name",text="Last Name")
        self.library_table.heading("Address 1",text="Address 1")
        self.library_table.heading("Address 2",text="Address 2")
        self.library_table.heading("ZIP",text="ZIP")
        self.library_table.heading("Mobile no",text="Mobile no")
        self.library_table.heading("Book ID",text="Book ID")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Author's Name",text="Author's Name")
        self.library_table.heading("Date Borrowed",text="Date Borrowed")
        self.library_table.heading("Date Due",text="Date Due")
        self.library_table.heading("Days on Book",text="Days on Book")
        self.library_table.heading("Late Return Fine",text="Late Return Fine")
        self.library_table.heading("Date over Due",text="Date over Due")
        self.library_table.heading("Actual Price",text="Actual Price")

        self.library_table['show']="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column('Member Type', width = 100)
        self.library_table.column("PRN no",width = 100)
        self.library_table.column("ID no",width = 100)
        self.library_table.column("First Name",width = 100)
        self.library_table.column("Last Name",width = 100)
        self.library_table.column("Address 1",width = 100)
        self.library_table.column("Address 2",width = 100)
        self.library_table.column("ZIP",width = 100)
        self.library_table.column("Mobile no",width = 100)
        self.library_table.column("Book ID",width = 100)
        self.library_table.column("Book Title",width = 100)
        self.library_table.column("Author's Name",width = 100)
        self.library_table.column("Date Borrowed",width = 100)
        self.library_table.column("Date Due",width = 100)
        self.library_table.column("Days on Book",width = 100)
        self.library_table.column("Late Return Fine",width = 100)
        self.library_table.column("Date over Due",width = 100)
        self.library_table.column("Actual Price",width = 100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="akshaya", database="LibraryManagementSystem")
        my_cursor =  conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                                    self.member_var.get(),
                                                                                                                    self.prn_var.get(),
                                                                                                                    self.id_var.get(),
                                                                                                                    self.fname_var.get(),
                                                                                                                    self.lname_var.get(),
                                                                                                                    self.address1_var.get(),
                                                                                                                    self.address2_var.get(),
                                                                                                                    self.zip_var.get(),
                                                                                                                    self.mobile_var.get(),
                                                                                                                    self.bookid_var.get(),
                                                                                                                    self.booktitle_var.get(),
                                                                                                                    self.author_var.get(),
                                                                                                                    self.dateborrowed_var.get(),
                                                                                                                    self.datedue_var.get(),
                                                                                                                    self.daysonbook_var.get(),
                                                                                                                    self.latereturnfine_var.get(),
                                                                                                                    self.dateoverdue_var.get(),
                                                                                                                    self.finalprice_var.get()

        ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Member added successfully!")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="akshaya", database="LibraryManagementSystem")
        my_cursor =  conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for items in rows:
                self.library_table.insert("", END,values=items)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.fname_var.set(row[3])
        self.lname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.zip_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showData(self):
        self.textBox.insert(END, "Member Type\t\t" + self.member_var.get() + "\n")
        self.textBox.insert(END, "PRN Number\t\t" + self.prn_var.get() + "\n")
        self.textBox.insert(END, "ID Number\t\t" + self.id_var.get() + "\n")
        self.textBox.insert(END, "First Name\t\t" + self.fname_var.get() + "\n")
        self.textBox.insert(END, "Last Name\t\t" + self.lname_var.get() + "\n")
        self.textBox.insert(END, "Address 1\t\t" + self.address1_var.get() + "\n")
        self.textBox.insert(END, "Address 2\t\t" + self.address2_var.get() + "\n")
        self.textBox.insert(END, "ZIP\t\t" + self.zip_var.get() + "\n")
        self.textBox.insert(END, "Mobile Number\t\t" + self.mobile_var.get() + "\n")
        self.textBox.insert(END, "Book ID\t\t" + self.bookid_var.get() + "\n")
        self.textBox.insert(END, "Book Title\t\t" + self.booktitle_var.get() + "\n")
        self.textBox.insert(END, "Author\t\t" + self.author_var.get() + "\n")
        self.textBox.insert(END, "Date Borrowed\t\t" + self.dateborrowed_var.get() + "\n")
        self.textBox.insert(END, "Date Due\t\t" + self.datedue_var.get() + "\n")
        self.textBox.insert(END, "Days on Book\t\t" + self.daysonbook_var.get() + "\n")
        self.textBox.insert(END, "Late Return Fune\t\t" + self.latereturnfine_var.get() + "\n")
        self.textBox.insert(END, "Date Over Due\t\t" + self.dateoverdue_var.get() + "\n")
        self.textBox.insert(END, "Actual Price\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.fname_var.set("")
        self.lname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.zip_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.textBox.delete("1.0", END)

    def iexit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="akshaya", database="LibraryManagementSystem")
        my_cursor =  conn.cursor()
        my_cursor.execute("update library set member_type=%s, id_no=%s, first_name = %s, last_name = %s, address1 = %s, address2 = %s, zip = %s, mobile_no = %s, book_id = %s, book_title = %s, author_name = %s, date_borrowed = %s, date_due = %s, days_on_book = %s, late_retuen_fee = %s, date_over_due = %s, actual_price = %s where PRN_NO=%s", (
                                                    self.member_var.get(),
                                                    self.id_var.get(),
                                                    self.fname_var.get(),
                                                    self.lname_var.get(),
                                                    self.address1_var.get(),
                                                    self.address2_var.get(),
                                                    self.zip_var.get(),
                                                    self.mobile_var.get(),
                                                    self.bookid_var.get(),
                                                    self.booktitle_var.get(),
                                                    self.author_var.get(),
                                                    self.dateborrowed_var.get(),
                                                    self.datedue_var.get(),
                                                    self.daysonbook_var.get(),
                                                    self.latereturnfine_var.get(),
                                                    self.dateoverdue_var.get(),
                                                    self.finalprice_var.get(),
                                                    self.prn_var.get()     
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated!")
    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get()=="":
            messagebox.showerror("Error", "First Select the Member!!!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="akshaya", database="LibraryManagementSystem")
            my_cursor =  conn.cursor()
            query = "delete from library where PRN_NO = %s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted!")



if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
