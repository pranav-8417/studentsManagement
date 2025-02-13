students = []  # List to store student records

while True:
    print("\n....Add Students Record....")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update Student Data")
    print("5. Delete Student Data")
    print("6. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        student_id = int(input("Enter student ID: "))
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_grade = input("Enter student grade: ")

        students.append({
            'id': student_id,
            'name': student_name,
            'age': student_age,
            'grade': student_grade
        })
        print("Student added successfully.")

    elif choice == 2:
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    elif choice == 3:
        student_id = int(input("Enter Student ID to search: "))
        found = False
        for student in students:
            if student['id'] == student_id:
                print(f"\nID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 4:
        student_id = int(input("Enter Student ID to update: "))
        for student in students:
            if student['id'] == student_id:
                student['name'] = input("Enter new name: ")
                student['age'] = int(input("Enter new age: "))
                student['grade'] = input("Enter new grade: ")
                print("Student record updated successfully.")
                break
        else:
            print("Student not found.")

    elif choice == 5:
        student_id = int(input("Enter Student ID to delete: "))
        for student in students:
            if student['id'] == student_id:
                students.remove(student)
                print("Student record deleted successfully.")
                break
        else:
            print("Student not found.")

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
