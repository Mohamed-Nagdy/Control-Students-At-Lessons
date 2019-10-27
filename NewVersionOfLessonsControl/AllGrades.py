'''
    Created By Mohamed Nagdy
    At 27-10-2019

    Program Description:
    This porgram to control the students in the lessons or in a school but it used in lessons more
    the teatcher can use this program to record the student informations like name and age and
    the days in the week he come init also
    and can also record the date of pay the month money and when it will finish
'''

from tkinter import *
import sqlite3 as sql
from tkinter import messagebox

# define the class of the school level
class Grade:
    # define all variables we will need in this program
    def __init__(self, tableName, windowTitle, editWindowTitle, createWindowTitle, showWindowTitle):
        self.tableName = tableName
        self.windowTitle = windowTitle
        self.editWindowTitle = editWindowTitle
        self.createWindowTitle = createWindowTitle
        self.showWindowTitle = showWindowTitle

        # declare the global elements which will use in the function submitRecord
        self.studentName = None
        self.age = None
        self.phone = None
        self.paymentMadeOn = None
        self.finishIn = None
        self.howMuchPaid = None
        self.daysOfWeek = None

        # this variables are used in delete and edit functions
        self.getId = None
        self.studentNameEdit = None
        self.ageEdit = None
        self.phoneEdit = None
        self.paymentMadeOnEdit = None
        self.finishInEdit = None
        self.howMuchPaidEdit = None
        self.daysOfWeekEdit = None

    # this function to create the Main window of the school level we need
    def gradeMainWindow(self):

        # create the window root with 330x300 width and height
        root = Tk()
        root.geometry('330x300')
        root.title(self.windowTitle)

        # Connect to database
        connect = sql.connect('StudyClass.db')

        # create the cursor
        cursor = connect.cursor()

        # create the table
        cursor.execute('CREATE TABLE IF NOT EXISTS ' + self.tableName + ' ( studentName text, age text, phone text, paymentMadeOn text, finishedIn text, howMuchPaid text, daysOfWeek text )')

        # create the Elements
        self.createNewRecord = Button(root, text='Create New Record', command=self.createNew)
        self.showAllRecord = Button(root, text='Show All Records', command=self.show)
        self.labelOfGetId = Label(root, text='ID To Edit Or Delete')
        self.getId = Entry(root)
        self.deleteRecord = Button(root, text='Delete Record', command=self.deleteRec)
        self.editRecord = Button(root, text='Edit Record', command=self.edit)

        # put the elements on the root container
        self.createNewRecord.grid(column=0, row=0, ipadx=100, padx=10, pady=2, ipady=10, columnspan=2)
        self.showAllRecord.grid(column=0, row=1, ipadx=105, padx=10, pady=2, ipady=10, columnspan=2)
        self.labelOfGetId.grid(column=0, row=2, ipadx=1, padx=10, pady=2, ipady=10)
        self.getId.grid(column=1, row=2, ipadx=1, padx=20, pady=2, ipady=10)
        self.deleteRecord.grid(column=0, row=3, ipadx=114, padx=10, pady=2, ipady=10, columnspan=2)
        self.editRecord.grid(column=0, row=4, ipadx=120, padx=10, pady=2, ipady=10, columnspan=2)

        connect.commit()
        connect.close()
        root.mainloop()

    # this function to create a new window to add new record to the database
    def createNew(self):

        # create the window secondary with 450x400 width and height
        secondary = Tk()
        secondary.geometry('450x400')
        secondary.title(self.createWindowTitle)

        # declare all the elements of the window
        self.studentName = Entry(secondary)
        self.age = Entry(secondary)
        self.phone = Entry(secondary)
        self.paymentMadeOn = Entry(secondary)
        self.finishIn = Entry(secondary)
        self.howMuchPaid = Entry(secondary)
        self.daysOfWeek = Entry(secondary)
        submit = Button(secondary, text='Submit', command=self.submitRecord)

        # labels for the entry boxes
        studentNameLabel = Label(secondary, text='Student Name')
        ageLabel = Label(secondary, text='Age')
        phoneLabel = Label(secondary, text='Phone')
        paymentMadeOnLabel = Label(secondary, text='Payment Made On')
        finishInLabel = Label(secondary, text='Finish In')
        howMuchPaidLabel = Label(secondary, text='How Much Paid')
        daysOfWeekLabel = Label(secondary, text='Days Of Week')

        # put all elements in the secondary window
        studentNameLabel.grid(column=0, row=0, padx=10, pady=2, ipady=10)
        self.studentName.grid(column=1, row=0, ipadx=80, padx=10, pady=2, ipady=10)

        ageLabel.grid(column=0, row=1, padx=10, pady=2, ipady=10)
        self.age.grid(column=1, row=1, ipadx=80, padx=10, pady=2, ipady=10)

        phoneLabel.grid(column=0, row=2, padx=10, pady=2, ipady=10)
        self.phone.grid(column=1, row=2, ipadx=80, padx=10, pady=2, ipady=10)

        paymentMadeOnLabel.grid(column=0, row=3, padx=10, pady=2, ipady=10)
        self.paymentMadeOn.grid(column=1, row=3, ipadx=80, padx=10, pady=2, ipady=10)

        finishInLabel.grid(column=0, row=4, padx=10, pady=2, ipady=10)
        self.finishIn.grid(column=1, row=4, ipadx=80, padx=10, pady=2, ipady=10)

        howMuchPaidLabel.grid(column=0, row=5, padx=10, pady=2, ipady=10)
        self.howMuchPaid.grid(column=1, row=5, ipadx=80, padx=10, pady=2, ipady=10)

        daysOfWeekLabel.grid(column=0, row=6, padx=10, pady=2, ipady=10)
        self.daysOfWeek.grid(column=1, row=6, ipadx=80, padx=10, pady=2, ipady=10)

        submit.grid(column=0, row=7, ipadx=80, padx=10, pady=2, ipady=10, columnspan=2)

        secondary.mainloop()

    # this function to insert the record to our database in the specific table
    def submitRecord(self):
        # Connect to database
        connect = sql.connect('StudyClass.db')

        # create the cursor
        cursor = connect.cursor()

        # this command used to take the entry boxes values and insert it in the table
        cursor.execute('INSERT INTO ' + self.tableName + ' VALUES ( :studentName, :age, :phone, :paymentMadeOn, :finishIn, :howMuchPaid, :daysOfWeek)',
            {
                'studentName': self.studentName.get(),
                'age': self.age.get(),
                'phone': self.phone.get(),
                'paymentMadeOn': self.paymentMadeOn.get(),
                'finishIn': self.finishIn.get(),
                'howMuchPaid': self.howMuchPaid.get(),
                'daysOfWeek': self.daysOfWeek.get()
            })

        # delete all the entry boxes component
        self.studentName.delete(0, END)
        self.age.delete(0, END)
        self.phone.delete(0, END)
        self.paymentMadeOn.delete(0, END)
        self.finishIn.delete(0, END)
        self.howMuchPaid.delete(0, END)
        self.daysOfWeek.delete(0, END)

        connect.commit()
        connect.close()

    # show all the records on a new screen in a table
    def show(self):
        # create the window secondary
        secondary = Tk()
        # secondary.geometry('800x400')
        secondary.title(self.showWindowTitle)

        # Connect to database
        connect = sql.connect('StudyClass.db')

        # create the cursor
        cursor = connect.cursor()

        cursor.execute('SELECT *, oid FROM ' + self.tableName)
        records = cursor.fetchall()

        # header of the table of the content of the Table in the database
        Label(secondary, text='Student Name', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=0)
        Label(secondary, text='Age', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=1)
        Label(secondary, text='Phone', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=2)
        Label(secondary, text='Payment Made On', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=3)
        Label(secondary, text='Finish In', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=4)
        Label(secondary, text='How Much Paid', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=5)
        Label(secondary, text='Days Of Week', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=6)
        Label(secondary, text='ID', relief=SUNKEN, bd=2, width=15, bg='yellow').grid(row=0, column=7)

        # display All Records in the database on the screen
        i = 2
        for record in records:
            Label(secondary, text=record[0], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=0)
            Label(secondary, text=record[1], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=1)
            Label(secondary, text=record[2], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=2)
            Label(secondary, text=record[3], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=3)
            Label(secondary, text=record[4], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=4)
            Label(secondary, text=record[5], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=5)
            Label(secondary, text=record[6], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=6)
            Label(secondary, text=record[7], relief=SUNKEN, bd=2, width=15, bg='white').grid(row=i, column=7)
            i += 1


        connect.commit()
        connect.close()
        secondary.mainloop()

    # this function is used to update the table record with id we specify
    def recording(self):
        # Connect to database
        connect = sql.connect('StudyClass.db')

        # create the cursor
        cursor = connect.cursor()

        cursor.execute('UPDATE ' + self.tableName + ' SET studentName= :studentName, age= :age, phone= :phone, paymentMadeOn= :paymentMadeOn, finishedIn= :finishIn, howMuchPaid= :howMuchPaid, daysOfWeek= :daysOfWeek WHERE oid=:oid',

            {
                'studentName': self.studentNameEdit.get(),
                'age': self.ageEdit.get(),
                'phone': self.phoneEdit.get(),
                'paymentMadeOn': self.paymentMadeOnEdit.get(),
                'finishIn': self.finishInEdit.get(),
                'howMuchPaid': self.howMuchPaidEdit.get(),
                'daysOfWeek': self.daysOfWeekEdit.get(),
                'oid': int(self.getId.get())
            })

        self.getId.delete(0, END)
        self.studentNameEdit.delete(0, END)
        self.ageEdit.delete(0, END)
        self.phoneEdit.delete(0, END)
        self.paymentMadeOnEdit.delete(0, END)
        self.finishInEdit.delete(0, END)
        self.howMuchPaidEdit.delete(0, END)
        self.daysOfWeekEdit.delete(0, END)

        connect.commit()
        connect.close()

    # this function is used to show the edit window
    def edit(self):

        # this for check if the id field is empty or not
        if self.getId.get() == '':
            messagebox.showinfo("No ID", 'Please Enter The Id First')
        else:
            # create the window secondary with 450x400 width and height
            secondary = Tk()
            secondary.geometry('450x400')
            secondary.title(self.editWindowTitle)

            # Connect to database
            connect = sql.connect('StudyClass.db')

            # create the cursor
            cursor = connect.cursor()

            # declare all the elements of the window
            self.studentNameEdit = Entry(secondary)
            self.ageEdit = Entry(secondary)
            self.phoneEdit = Entry(secondary)
            self.paymentMadeOnEdit = Entry(secondary)
            self.finishInEdit = Entry(secondary)
            self.howMuchPaidEdit = Entry(secondary)
            self.daysOfWeekEdit = Entry(secondary)
            edit = Button(secondary, text='Edit', command=self.recording)

            # this command to get all fields from the table
            cursor.execute('SELECT * FROM ' + self.tableName + ' WHERE oid=' + self.getId.get())

            # set all the fields in the records variable
            records = cursor.fetchall()

            # set all the fields of every record in the entry boxes
            for record in records:
                self.studentNameEdit.insert(0, record[0])
                self.ageEdit.insert(0, record[1])
                self.phoneEdit.insert(0, record[2])
                self.paymentMadeOnEdit.insert(0, record[3])
                self.finishInEdit.insert(0, record[4])
                self.howMuchPaidEdit.insert(0, record[5])
                self.daysOfWeekEdit.insert(0, record[6])

            # labels for the entry fields
            studentNameLabel = Label(secondary, text='Student Name')
            ageLabel = Label(secondary, text='Age')
            phoneLabel = Label(secondary, text='Phone')
            paymentMadeOnLabel = Label(secondary, text='Payment Made On')
            finishInLabel = Label(secondary, text='Finish In')
            howMuchPaidLabel = Label(secondary, text='How Much Paid')
            daysOfWeekLabel = Label(secondary, text='Days Of Week')

            # put all elements in the secondary window
            studentNameLabel.grid(column=0, row=0, padx=10, pady=2, ipady=10)
            self.studentNameEdit.grid(column=1, row=0, ipadx=80, padx=10, pady=2, ipady=10)

            ageLabel.grid(column=0, row=1, padx=10, pady=2, ipady=10)
            self.ageEdit.grid(column=1, row=1, ipadx=80, padx=10, pady=2, ipady=10)

            phoneLabel.grid(column=0, row=2, padx=10, pady=2, ipady=10)
            self.phoneEdit.grid(column=1, row=2, ipadx=80, padx=10, pady=2, ipady=10)

            paymentMadeOnLabel.grid(column=0, row=3, padx=10, pady=2, ipady=10)
            self.paymentMadeOnEdit.grid(column=1, row=3, ipadx=80, padx=10, pady=2, ipady=10)

            finishInLabel.grid(column=0, row=4, padx=10, pady=2, ipady=10)
            self.finishInEdit.grid(column=1, row=4, ipadx=80, padx=10, pady=2, ipady=10)

            howMuchPaidLabel.grid(column=0, row=5, padx=10, pady=2, ipady=10)
            self.howMuchPaidEdit.grid(column=1, row=5, ipadx=80, padx=10, pady=2, ipady=10)

            daysOfWeekLabel.grid(column=0, row=6, padx=10, pady=2, ipady=10)
            self.daysOfWeekEdit.grid(column=1, row=6, ipadx=80, padx=10, pady=2, ipady=10)

            edit.grid(column=0, row=7, ipadx=80, padx=10, pady=2, ipady=10, columnspan=2)

            connect.commit()
            connect.close()
            secondary.mainloop()

    # this function is used for delete any field we specify it's id
    def deleteRec(self):

        # this for check if the id field is empty or not
        if self.getId.get() == '':
            messagebox.showinfo("No ID", 'Please Enter The Id First')
        else:
            # Connect to database
            connect = sql.connect('StudyClass.db')

            # create the cursor
            cursor = connect.cursor()

            # show message box to ask the user if he really need to delete this record
            result = messagebox.askyesno('Delete Record', 'You Sure You Want To Delete It ?')

            # if he click yes it will deleted
            if result == 1:
                # this command for delete the record
                cursor.execute('DELETE FROM ' + self.tableName + ' WHERE oid=' + self.getId.get())
            # delete what ever in the id entry field
            self.getId.delete(0, END)

            connect.commit()
            connect.close()
