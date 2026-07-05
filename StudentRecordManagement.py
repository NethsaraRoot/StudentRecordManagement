# Student Record Management System

students = []


def get_marks(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} Marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Enter a number.")


def add_student():
    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")

    programming = get_marks("Programming")
    database = get_marks("Database")
    networking = get_marks("Networking")

    average = (programming + database + networking) / 3

    status = "Pass" if average >= 50 else "Fail"

    student = {
        "id": student_id,
        "name": name,
        "programming": programming,
        "database": database,
        "networking": networking,
        "average": average,
        "status": status
    }

    students.append(student)
    print("Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n================ STUDENT LIST ================\n")

    for student in students:
        print(f"ID          : {student['id']}")
        print(f"Name        : {student['name']}")
        print(f"Programming : {student['programming']}")
        print(f"Database    : {student['database']}")
        print(f"Networking  : {student['networking']}")
        print(f"Average     : {student['average']:.2f}")
        print(f"Status      : {student['status']}")
        print("-------------------------------------------")

    print("Total Students :", len(students))


def search_student():
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("\nStudent Found")
            print(student)
            return

    print("Student not found.")


def calculate_average():
    if len(students) == 0:
        print("No records available.")
        return

    for student in students:
        print(student["name"], "Average =", round(student["average"], 2))


def highest_student():
    if len(students) == 0:
        print("No records available.")
        return

    top = max(students, key=lambda x: x["average"])

    print("\nHighest Scoring Student")
    print("ID      :", top["id"])
    print("Name    :", top["name"])
    print("Average :", round(top["average"], 2))


def sort_students():
    if len(students) == 0:
        print("No records available.")
        return

    sorted_students = sorted(students, key=lambda x: x["average"], reverse=True)

    print("\nStudents Sorted by Average Marks")

    for student in sorted_students:
        print(student["name"], "-", round(student["average"], 2))


while True:

    print("\n========== Student Record Management ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Calculate Average Marks")
    print("5. Display Highest Scoring Student")
    print("6. Sort Students by Average")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        highest_student()

    elif choice == "6":
        sort_students()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")