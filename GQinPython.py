##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
# code here
grades = {}

# Loop until the user chooses to quit.
# Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
# Prevent unexpected inputs by converting input to upper-case
# code here
check = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Quit)? ")
check = check.upper()
exit = False
while not exit:

    # Use a condition to handle adding a new student.
    # Convert grade into integer
    # Gather user input for "Enter the name of the student: "
    # Check if student name already exists "Sorry, that student is already present."
    # Gather user input for student grade "Enter the student's grade: "
    # code here
    if check == 'A':
        name = input("Enter the name of the student: ")
        if name in grades:
            print("Sorry, that student is already present")
            continue
        grade = int(input("Enter the student's grade: "))
        grades[name] = grade
        check = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Quit)? ")
        check = check.upper()

    # Handle removing a student if user inputs 'R'
    # Check input for "What student do you want to remove? "
    # use pop to remove key/value form grades
    # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
    # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
    # code here
    elif check == 'R':
        erase = input("What student do you want to remove? ")
        if erase not in grades:
            print("Sorry, that student doesn't exist and couldn't be removed.")
            continue
        grades.pop(erase)
        check = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Quit)? ")
        check = check.upper()

    # Handle modifying a student grade if user inputs 'M'
    # "Enter the name of the student to modify: "
    # Convert grade into integer
    # If student is in grades dictionary, show existing grade "The old grade is"
    # Gather input for new grade "Enter the new grade: "
    # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
    # code here
    elif check == 'M':
        mod = input("Enter the name of the student to modify: ")
        if mod in grades:
            print("The old grade is", grades[mod])
            newG = int(input("Enter the new grade: "))
            grades[mod] = newG
            check = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Quit)? ")
            check = check.upper()
        elif mod not in grades:
            print("Sorry, that student doesn't exist and couldn't be modified")
            continue

    # Handle printing grade average as a string if user input is 'P'
    # Use "The average grade is "
    # Handle printing all of the student names with associated grade
    # Display explicitly as strings
    # code here
    elif check == 'P':
        total = 0
        count = len(grades)
        for grade in grades.values():
            total += grade
        avg = total / count
        print("The average grade is %.2f" % avg)
        for name, grade in grades.items():
            nameS = str(name)
            gradeS = str(grade)
            print(nameS, ":", gradeS)
        check = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Quit)? ")
        check = check.upper()



    # Handle the case for quiting if user inputs 'Q' "Goodbye!"
    # code here
    elif check == 'Q':
        print("Goodbye!")
        exit = True

    # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
    # code here
    else:
        print("Sorry, that wasn't a valid choice. ")
        check = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Quit)? ")
        check = check.upper()
