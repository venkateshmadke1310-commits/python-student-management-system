filename = "students.txt"

def load_students():
    students = []
    

    try: 
        with open(filename, "r") as file:
            for line in file:
                roll, name, course, marks = line.strip().split("|")
                
                students.append({
                    "roll" : roll,
                    "name" : name,
                    "course" : course,
                    "marks" : marks
                })
    except FileNotFoundError:
         pass

    return students

def save_students(students):
    with open(filename, "w") as file:
        for student in students:
           line = f"{student['roll']}|{student['name']}|{student['course']}|{student['marks']}\n"
           file.write(line)

def add_student(students):
    st_roll = input("Roll No: ")
    st_name = input("Student name: ")
    st_course = input("Course: ")
    st_marks = input("Marks: ")

    for student in students:
        if student["roll"] == st_roll:
            print("Student with this roll number already exist")
            return

    students.append({"roll": st_roll, 
                     "name": st_name, 
                     "course": st_course, 
                     "marks": st_marks
                    }) 
    save_students(students)
    print("Student added successfully.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    
    print("\n  Student List  ")
    for student in students:
        print(f"Roll No : {student['roll']}")
        print(f"Name : {student['name']}")
        print(f"Course : {student['course']}")
        print(f"Marks : {student['marks']}")
        print("-" * 20)

def search_student(students):
    search_roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == search_roll:
            print("\nStudent Found:")
            print(f"Roll No : {student['roll']}")
            print(f"Name : {student['name']}")
            print(f"Course : {student['course']}")
            print(f"Marks : {student['marks']}")
            return
        
    print("Student not found. ")

def update_student(students):
    search_roll = input("Enter roll number to update: ")

    for student in students:
        if student["roll"] == search_roll:
            print("\nCurrent Details:")
            print(f"Name   : {student['name']}")
            print(f"Course : {student['course']}")
            print(f"Marks  : {student['marks']}")

            new_name = input("Enter new name (leave blank to keep same)")
            new_course = input("Enter new course (leave blank to keep same) ")
            new_marks = input("Enter new marks (leave blank to keep same)")

            if new_name:
                student['name'] = new_name
            if new_course:
                student['course'] = new_course
            if new_marks:
                student['marks'] = new_marks

            save_students(students)
            print("Student updated successfully.")
            return 

    print("Student not found.")

def delete_student(students):
    search_roll = input("Enter roll number to delete: ")
    for student in students:
        if student["roll"] == search_roll:
             students.remove(student)
             save_students(students) 
             print("Student deleted successfully. ")
             return 
    print("Student not found")

def menu():
        print("\n--STUDENT MANAGEMENT SYSTEM--")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

students = load_students()

while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again. ")