# Student Management System

This project is my **Python Student Management System**, created as the end project for our Python module.  

The main purpose of the system is to help an admin or teacher manage student records easily. With this program, we can:  
- Add new student details like Name, Age, Department, and Marks.  
- Automatically generate Roll Numbers (so no need to type them manually).  
- View all student records in a clear format.  
- Update or delete a student’s record using their Roll Number.  
- Search for students by name or by department.  
- See the top-performing students by marks (the program lets you choose how many top students user want to see).  
- Keep track of when each student was added using the date and time.  

To make sure the data is not lost, I used **file handling**. All student records are stored in a CSV file (`students.csv`), and every time the program runs, it loads the data back from the file. This way, the data is saved permanently even after you close the program.  

The project is divided into three main Python files:  
- **login.py** - manages login with a simple username and password.  
- **add.py** - contains all the functions for adding, viewing, updating, deleting, and searching students.  
- **main.py** - acts as the central file where the menu is displayed and different features are connected.  

To run the program, just open the folder in Python or VS Code, and run `main.py`. Then log in with the predefined username and password (set inside `login.py`).  

This project helped me practice important Python concepts such as:  
- Functions and modular programming  
- File handling with CSV  
- Using `datetime` to record entry times  
- Exception handling for invalid inputs  

I really enjoyed building this project because it feels like a real-life application of Python, not just small programs.  
