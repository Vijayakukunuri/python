def add_student():
    student_id = input("Enter student ID: ")
    studentname = input("Enter student name: ")
    studentgrade = input("Enter student grade: ")
    studentmarks = input("enter the total  marks : ")
    studentclass = input("enter the  classs : ")

    with open("C:\\Users\Lenovo\Desktop\\vijju\studentdata\studentlist.txt", "a+") as file:
        file.write(f"{student_id} , {studentname} , {studentgrade} , {studentmarks} , {studentclass}\n")
    print("Student record added successfully.")


while True:
    print("\nStudent Data Management System")
    print("1. Add Student")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please enter 1, 2")



