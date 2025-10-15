def authentic():
    admin_name = "admin1234"
    admin_password = "admin@1234"

    teacher_name = "teacher1234"
    teacher_password = "teacher@1234"

    print("Student Management Portal")

    for i in range(3):  # 3 attempts
        user = input(" USER ID: ")
        password = input("password: ")

        if user == admin_name and password == admin_password:
            print("\nLogin successful! You are logged in as ADMIN.\n")
            return "admin"

        elif user == teacher_name and password == teacher_password:
            print("\nLogin successful! You are logged in as TEACHER.\n")
            return "teacher"

        else:
            print("Invalid login. Try again.\n")

    print("Too many failed attempts! Exiting...")
    return None
