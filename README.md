# Student Result Processing System

## Project Overview

The Student Result Processing System is a Python-based application designed to manage student academic records and generate examination reports. It uses text file handling to store, retrieve, update, and process student information.

The system calculates total marks, percentages, and grades, and provides class performance statistics.

## Features

- Add records for multiple students.
- Store student details using text files.
- Display all student records.
- Search students by roll number.
- Modify existing student records.
- Calculate total marks, percentage, and grades.
- Display the topper list in descending order.
- Calculate class average, highest marks, and lowest marks.
- Generate and append final result reports to a text file.

## Technologies Used

- **Programming Language:** Python
- **Concepts:** File Handling, Functions, Lists, Dictionaries, Loops, Conditional Statements, Lambda Functions, and Sorting.
- **Storage:** Text Files (`.txt`)

## Project Structure

```text
Student-Result-Processing-System/
│
├── main.py
├── students.txt
├── result.txt
└── README.md
```

- `main.py` – Main Python application.
- `students.txt` – Stores student records.
- `result.txt` – Stores generated result reports.
- `README.md` – Project documentation.

*Note: The text files are created automatically when required by the program.*

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in Python IDLE or VS Code.
4. Run the `main.py` file.
5. Select the required operation from the menu.

## Result Calculation

The system calculates:

- **Total Marks:** Sum of marks obtained in three subjects.
- **Percentage:** Total Marks / 300 × 100.
- **Grade:** Assigned according to the percentage.

## Learning Outcomes

Through this project, I practised:

- Python file handling using `open()`, `with`, `write()`, `writelines()`, `readline()`, and `readlines()`.
- Creating and using Python functions.
- Managing data using lists and dictionaries.
- Searching, sorting, and modifying records.
- Performing basic data calculations and generating reports.

##
