from datetime import datetime
students = []
def auto_roll_no():
    #Return the next roll number automatically.
    if len(students) > 0:
        highest = 0
        for s in students:
            # Converting the roll number (string) to an integer
            roll = int(s["Roll No"])
    
            if roll > highest:
                # update highest
                highest = roll
        # add 1 to the highest roll number
        next_roll = highest + 1
        return str(next_roll)
    else:
        
        return "1"
# ADD NEW STUDENT RECORD - STEP_2
def add_students():

    print("Welcome to add new student portal : ")
    name = input("Enter the student name : ")
    roll_no = auto_roll_no()
    age = input("Enter the age of the student : ")
    dept = input("Enter the department : ")
    marks = input("Enter the marks : ")

    time_entry = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

    student = {"Name":name,
               "Roll No":roll_no, 
               "Age":age, 
               "Department":dept,
               "Marks":marks,
               "Entry Time":time_entry}

    students.append(student)
    print("Student Name Added Successfully.")
    print(f"{name} is added to Student portal")
# VIEW STUDENT RECORD - STEP_3
def view_students():
    print(" Student Records ")

    if not students:
        print("No records found.")
    else:
        for s in students:
            print(
                f"Name: {s['Name']},Roll No: {s['Roll No']}, Age: {s['Age']}, "
                f"Department: {s['Department']}, Marks: {s['Marks']}, Entry: {s['Entry Time']}"
            )
# UPDATE STUDENT DETAILS - STEP_4
def update_student():
    # Update any student detail based on Roll Number.
    print("\n=== Update Student Details ===")

    if not students:
        print("No records found.")
        return

    roll_no = input("Enter the Roll Number of the student to update: ")

    # find the student
    for s in students:
        if s["Roll No"] == roll_no:
            print(f"Found student: {s['Name']} (Roll No: {roll_no})")

            # Asking what to update
            print("What do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Department")
            print("4. Marks")

            choice = input("Enter choice: ")

            if choice == "1":
                new_name = input("Enter new name: ")
                s["Name"] = new_name
            elif choice == "2":
                new_age = input("Enter new age: ")
                s["Age"] = new_age
            elif choice == "3":
                new_dept = input("Enter new department: ")
                s["Department"] = new_dept
            elif choice == "4":
                new_marks = input("Enter new marks: ")
                s["Marks"] = new_marks
            else:
                print("Invalid choice.")

            print("Student details updated successfully!")
            return  # exit function after updating

    # if roll number not found
    print("Student with that Roll Number not found.")
# DELETE STUDENT RECORD - STEP_5_
def delete_student():
    # Delete a student record based on Roll Number.
    print(" Delete Student Record ")

    if not students:
        print("No records found.")
        return

    roll_no = input("Enter the Roll Number of the student to delete: ")


    for s in students:
     
     if s["Roll No"] == roll_no:
        student_name = s["Name"]  # store the name
        students.remove(s)
        print(f"Student {student_name} with Roll No {roll_no} deleted successfully!")
        return

print("Student with that Roll Number not found.")
students = []  # main list

# FILE HANDLING - STEP_7
import csv

students = []

def save_students_to_file():
    #Save students to a CSV file safely.
    with open("students.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Roll No", "Name", "Age", "Department", "Marks", "Entry Time"]
        )
        writer.writeheader()
        writer.writerows(students)

def load_students_from_file():
    #Load students from CSV File
    loaded = []
    try:
        with open("students.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                loaded.append(row)
    except FileNotFoundError:
        pass
    return loaded
# SEARCH STUDENT BY NAME OR DEPARTMENT - STEP_8
def search_student():
    #Search for students by name or department.
    print(" Search Student ")

    if not students:
        print("No records found.")
        return

    print("Search by:")
    print("1. Name")
    print("2. Department")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name to search: ").lower()
        found = False
        for s in students:
            if s["Name"].lower() == name:
                print(f"Roll No: {s['Roll No']}, Name: {s['Name']}, Department: {s['Department']}")
                found = True
        if not found:
            print("No student found with that name.")

    elif choice == "2":
        dept = input("Enter department to search: ").lower()
        found = False
        for s in students:
            if s["Department"].lower() == dept:
                print(f"Roll No: {s['Roll No']}, Name: {s['Name']}, Department: {s['Department']}")
                found = True
        if not found:
            print("No student found in that department.")
    else:
        print("Invalid choice.")
# VIEW TOP-PERFORMING STUDENTS BY USER INPUT
def view_top_students():
    #Show top students based on marks.
    if not students:
        print("No student records to show.")
        return

    # taking input from user how many top students want
    try:
        limit = int(input("How many top students do you want to see? "))
    except ValueError:
        print("Invalid number.")
        return

    # sorting students by Marks (converted to int)
    sorted_students = sorted(students, key=lambda s: int(s['Marks']), reverse=True)

    print(f"\nTop {limit} Students:")
    # looping through the top `limit` students
    for s in sorted_students[:limit]:
        print(f"Roll No: {s['Roll No']}, Name: {s['Name']}, Marks: {s['Marks']}")







   


    