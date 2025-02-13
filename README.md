# Student Grades Manager in C++ and Python

### Overview

This C++ program is a grades manager that allows users to add, remove, modify, and display student grades. The grades are stored in a dictionary-like data structure, where the student's name is the key and their grade is the value. The program also calculates the average grade of all students.

### Features
* Add a student with their grade
* Remove a stufent from the list
* Modify an existing student's grade
* Print all students' grades + class avg
* Quit the program

### How it Works
1. The user is prompted with options: (A )dd, (R ) emove, (M )odify, (P )rint all, or (Q )uit.
2. Based on the letter entered:
* Add (A): Enter a student's name and grade. If the student already exists, an error is displayed.
* Remove (R): Enter the student's name to remove them. If they don’t exist, an error is shown.
* Modify (M): Enter the student’s name to update their grade. If they don’t exist, an error is displayed.
* Print (P): Displays all students and their grades, along with the average grade.
* Quit (Q): Exits the program.
