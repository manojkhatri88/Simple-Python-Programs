student = {}

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add students")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter the student name: ")
        marks = int(input("Enter the marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")
    
    #view Students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)
    
    #check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        
        else:
            print("Student not found!")

    # exit
    elif choice == "4":
        print("Exiting....")
        break

    else:
        print("In-valid Input!")