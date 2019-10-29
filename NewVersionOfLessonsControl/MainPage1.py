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
from AllGrades import *

root = Tk()
#root.geometry('350x400')
root.title('Mr Mahmoud Ali Program')
root.resizable(False, False)

# for Primary School Students
firstGradeObject = Grade('firstGrade', 'First Grade Main Window', 'First Grade Edit Window', 'First Grade Create New Student Window', 'First Grade Show All Records Window')
secondGradeObject = Grade('secondGrade', 'Second Grade Main Window', 'Second Grade Edit Window', 'Second Grade Create New Student Window', 'Second Grade Show All Records Window')
thirdGradeObject = Grade('thirdGrade', 'Third Grade Main Window', 'Third Grade Edit Window', 'Third Grade Create New Student Window', 'Third Grade Show All Records Window')
fourthGradeObject = Grade('fourthGrade', 'Fourth Grade Main Window', 'Fourth Grade Edit Window', 'Fourth Grade Create New Student Window', 'Fourth Grade Show All Records Window')
fifthGradeObject = Grade('fifthGrade', 'Fifth Grade Main Window', 'Fifth Grade Edit Window', 'Fifth Grade Create New Student Window', 'Fifth Grade Show All Records Window')
sixthGradeObject = Grade('sixthGrade', 'Sixth Grade Main Window', 'Sixth Grade Edit Window', 'Sixth Grade Create New Student Window', 'Sixth Grade Show All Records Window')

# for Preparatory School Students
firstPrepGradeObject = Grade('firstPrep', 'First Prep Grade Main Window', 'First Prep Grade Edit Window', 'First Prep Grade Create New Student Window', 'First Prep Grade Show All Records Window')
secondPrepGradeObject = Grade('secondPrep', 'Second Prp Grade Main Window', 'Second Prp Grade Edit Window', 'Second Prp Grade Create New Student Window', 'Second Prp Grade Show All Records Window')
thirdPrepGradeObject = Grade('thirdPrep', 'Third Prep Grade Main Window', 'Third Prep Grade Edit Window', 'Third Prep Grade Create New Student Window', 'Third Prep Grade Show All Records Window')

# for Secondary School Students
firstSecGradeObject = Grade('firstSec', 'First Secondary Grade Main Window', 'First Secondary Grade Edit Window', 'First Secondary Grade Create New Student Window', 'First Secondary Grade Show All Records Window')
secondSecGradeObject = Grade('secondSec', 'Second Secondary Grade Main Window', 'Second Secondary Grade Edit Window', 'Second Secondary Grade Create New Student Window', 'Second Secondary Grade Show All Records Window')
thirdSecGradeObject = Grade('thirdSec', 'Third Secondary Grade Main Window', 'Third Secondary Grade Edit Window', 'Third Secondary Grade Create New Student Window', 'Third Secondary Grade Show All Records Window')


# declare all Elements
# For Primary School
firsGrade = Button(root, text='First Grade', command=firstGradeObject.gradeMainWindow)
secondGrade = Button(root, text='Second Grade', command=secondGradeObject.gradeMainWindow)
thirdGrade = Button(root, text='Third Grade', command=thirdGradeObject.gradeMainWindow)
fourthGrade = Button(root, text='Fourth Grade', command=fourthGradeObject.gradeMainWindow)
fifthGrade = Button(root, text='Fifth Grade', command=fifthGradeObject.gradeMainWindow)
sixthGrade = Button(root, text='Sixth Grade', command=sixthGradeObject.gradeMainWindow)

# For Preparatory School
firstPrep = Button(root, text='First Preparatory', command=firstPrepGradeObject.gradeMainWindow)
secondPrep = Button(root, text='Second Preparatory', command=secondPrepGradeObject.gradeMainWindow)
thirdPrep = Button(root, text='Third Preparatory', command=thirdPrepGradeObject.gradeMainWindow)

# for Secondary School
firstSec = Button(root, text='First Secondary', command=firstSecGradeObject.gradeMainWindow)
secondSec = Button(root, text='Second Secondary', command=secondSecGradeObject.gradeMainWindow)
thirdSec = Button(root, text='Third Secondary', command=thirdSecGradeObject.gradeMainWindow)

# put all elements on the root container
# For Primary School
firsGrade.grid(column=0, row=0, ipadx=67, padx=10, pady=2, ipady=10)
secondGrade.grid(column=1, row=0, ipadx=60, padx=10, ipady=10, pady=2)
thirdGrade.grid(column=2, row=0, ipadx=65, padx=10, ipady=10, pady=2)
fourthGrade.grid(column=0, row=1, ipadx=60, padx=10, ipady=10, pady=2)
fifthGrade.grid(column=1, row=1, ipadx=68, padx=10, ipady=10, pady=2)
sixthGrade.grid(column=2, row=1, ipadx=65, padx=10, ipady=10, pady=2)

Label(root, width=100, bg='black').grid(row=2, columnspan=3)

# For Preparatory School
firstPrep.grid(column=0, row=3, ipadx=52, padx=10, ipady=10, pady=2)
secondPrep.grid(column=1, row=3, ipadx=45, padx=10, ipady=10, pady=2)
thirdPrep.grid(column=2, row=3, ipadx=50, padx=10, ipady=10, pady=2)

Label(root, width=100, bg='black').grid(row=4, columnspan=3)

# For Secondary School
firstSec.grid(column=0, row=5, ipadx=55, padx=10, ipady=10, pady=2)
secondSec.grid(column=1, row=5, ipadx=50, padx=10, ipady=10, pady=2)
thirdSec.grid(column=2, row=5, ipadx=53, padx=10, ipady=10, pady=2)

root.mainloop()
