from login import authentic
from add import*

def main():
    #  Load data from file at start
    students.extend(load_students_from_file())

    role = authentic()
    if role is None:
        return

    print(f"\nWelcome to the Student Management System, {role.upper()}!")

    while True:
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. View Top Performing Students")
        print("7. Exit")


        choice = input("Enter choice: ")

        if choice == "1":
            add_students()
            save_students_to_file()  #  Save after add

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()
            save_students_to_file()  #  Save after update

        elif choice == "4":
            delete_student()
            save_students_to_file()  # Save after delete

        elif choice == "5":
            search_student()
        
        elif choice == "6":
            view_top_students()
        
        elif choice == "7":

    
            print("Exiting... Goodbye!")
            save_students_to_file()  #  Save before exit
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
