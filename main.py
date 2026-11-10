#Student Result Management System
import os

SUBJECTS = ['subject 1','subject 2','subject 3']

#1. Load Student Records
def load_students():

    students = []

    if not os.path.exists('students.txt'):
        return students

    with open('students.txt','r') as file:

        header = file.readline()
        lines = file.readlines()

        for line in lines:

            data = line.strip().split('|')

            if len(data) == 5:

                student = {

                    'roll':data[0],
                    'name':data[1],
                    'marks':[
                        int(data[2]),
                        int(data[3]),
                        int(data[4])
                        ]
                    }
                students.append(student)
                
        return students 

#Calculate Total,Percentage and Grade

def calculate_result(student):

    total = sum(student['marks'])
    percentage = (total/300)*100

    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'c'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'

    student['total'] = total
    student['percentage'] = percentage
    student['grade'] = grade

    return student

#Add Students Records
def add_students():

    students = load_students()

    n = int(input('How many students to add?'))

    new_records = []

    for i in range(n):

        print('\nEnter Student',i+1,'Details')

        roll = input('Enter Roll Number: ')
        

        if any(s['roll'] == roll for s in students):
             print('roll number already exits!')
             continue

        name = input('Enter student Name: ')

        marks = []

        for subject in SUBJECTS:

            while True:
                mark = int(input('Enter your' + subject + 'marks:'))

                if 0<= mark <=100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be Between 0 and 100!")

        record = roll +'|'+ name + '|'

        record = record + '|'.join(map(str,marks)) +'\n'

        new_records.append(record)

        students.append({
                'roll':roll,
                'name':name,
                'marks':marks
                })
    with open('students.txt','a') as file:

        if file.tell()== 0:
            file.write("Roll|Name|Sub1|Sub2|Sub3\n")

        file.writelines(new_records)

    print('Student record saved successfully!')

#Display all Students
def display_students():

    students = load_students()

    if len(students) == 0:
        print('No Students record found!')
        return

    print('====== STUDENT RECORDS ======')

    for student in students:

        calculate_result(student)

        print('Roll Number:',student['roll'])
        print('Name:',student['name'])
        print('Marks:',student['marks'])
        print('Total:',student['total'])
        print('Percentage:',round(student['percentage'],2),'%')
        print('Grade:',student['grade'])

#Search Student by Roll Number
def search_student():

    students = load_students()
    roll = input('Enter roll no to search: ')

    for student in students:

        if student['roll'] == roll:
            calclate_result(student)

        print('Roll Number:',student['roll'])
        print('Name:',student['name'])
        print('Marks:',student['marks'])
        print('Total:',student['total'])
        print('Percentage:',round(student['percentage'],2),'%')
        print('Grade:',student['grade'])

        return

    print('Student Not Found')

#Modify Student Record
def modify_student():

    students = load_student()

    roll = input('Enter roll no to modify:')

    for student in students:

        if student['roll'] == roll:
            print('Student Found!')

            print('Current Name: ',student['name'])

            student['name'] = input('Enter New Name:')

            print('\n Enter Updated Marks: ')

            for subject in SUBJECT:

                while True:

                    mark = int(input('Enter'+ subject +'marks:'))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print('Mark must be between 0 and 100!')

            student['marks'] = marks

            #Update the complete File

            save_students(students)
            print('Student Record Updated Successfully!')
            return

        print('Student not found!')

#Function to rewrite Updated Records
def save_students(students):

    with open('students.txt','w') as file:
        print('roll|Name|sub1|sub2|sub3\n')

        records = []

        for student in students:

            record = student['roll']+ '|'
            record += student['name']+'|'
            record += "|" .join(map(str,student['marks'])) + "\n"

            records.append(record)

        file.writelines(records)

#Display Topper List
def topper_list():

    students = load_students()

    if len(students) == 0:
        print('No records found!')
        return

    for student in students:
        calculate_result(student)

        #sort by total mark
        student.sort(key = lambda x:x['total'],reverse = True)

        print('====== Topper List ======')

        for student in students:

            students = {
                student['roll'],
                student['name'],
                student['total'],
                student['grade']
                }

#Class Statistics
def class_statistics():

    students = load_students()

    if len(students) == 0:
        print('No records available!')
        return

    totals = []

    for student in students:
        calculate_result(student)

        totals.append(student['total'])

        average = sum(totals)/len(totals)

        highest = max(totals)
        lowest = min(totals)

        print("\n========== CLASS STATISTICS ==========")

        print("Total Students:", len(students))
        print("Class Average:", round(average, 2))
        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)


#Generate Final Report
def generate_report():

    students = load_students()

    if len(students) == 0:
        print('No records found!')
        return

    for student in students:
        calculate_result(student)

    students.sort(key=lambda x:x['total'],
                  reverse = True
                  )

    totals = [s['total'] for s in students]

    average = sum(totals)/len(totals)

    #Append Final Result
    with open('result.txt','a') as file:
        file.write('====== FINAL RESULT REPORT ======')

        for student in students:
            
            

            report = (
               f'roll no: {student['roll']} |'
               f'Name: {student['name']} |'
               f'Total: {student['total']} |'
               f'Percentage: {student['percentage']:.2f}% |'
               f'Grade: {student['grade']}\n'
            )
            file.write(report)

        file.write("\nClass Average: " + str(round(average, 2)))
        file.write("\nHighest Marks: " + str(max(totals)))
        file.write("\nLowest Marks: " + str(min(totals)))

        file.write("\n==========================================\n")

print("\nFinal result report saved in result.txt!")

#Main - Menu
while True:

    print('\n====== Student Result System ======')
    print('1. Add Student Records')
    print('2. Display all Student Records')
    print('3. Search Student')
    print('4. Modify Student Records')
    print('5. Display Topper List')
    print('6. Class Statistics')
    print('7. Generate Final Result Report')
    print('8. Exit')

    choise = int(input('Enter your Chosie: '))

    if choise == 1:
        add_students()
    elif choise == 2:
        display_students()
    elif choise == 3:
        search_students()
    elif choise == 4:
        modify_student()
    elif choise == 5:
        topper_list()
    elif choise == 6:
        class_statistics()
    elif choise == 7:
        generate_report()
    elif choise == 8:
        print('Thank you for chossing Student result system!')
        break
    else:
        print('Enter valid Choise!!')









        

    
