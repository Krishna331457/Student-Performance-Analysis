# Student Performance Analytics System

A Python-based data analysis project that reads student records from a CSV file, calculates academic performance metrics, assigns grades, and generates a summarized performance report.

## Overview

This project is designed for academic data analysis and reporting. It processes student marks across five subjects, analyzes class performance, checks pass/fail status, and saves the final report in CSV format for further use.

The application reads the dataset from `students.csv`, computes derived fields such as total marks and average marks, and prints a formatted summary in the terminal.

## Features

- Load student data from CSV
- Calculate total marks and average marks
- Assign grades based on academic performance
- Determine pass/fail status for each student
- Compute class-level statistics
- Evaluate subject-wise averages
- Display the top-performing students
- Calculate average attendance
- Save final processed results to `student_performance_report.csv`

## Project Structure

```text
EWB Project/
├── main.py
├── students.csv
├── student_performance_report.csv
├── README.md
└── .gitignore (if present)
```

## Technologies Used

- Python
- Pandas
- NumPy

## Dataset

The input file is `students.csv` and includes the following columns:

| Column | Description |
| --- | --- |
| Student_ID | Unique student identifier |
| Name | Student name |
| Department | Academic department or branch |
| Python | Marks in Python |
| SQL | Marks in SQL |
| Java | Marks in Java |
| CSS | Marks in CSS |
| JavaScript | Marks in JavaScript |
| Attendance | Attendance percentage |

## Grade Rules

The project uses the following grade scale:

| Average Score | Grade |
| --- | --- |
| 90 and above | O |
| 80 to 89.99 | A+ |
| 70 to 79.99 | A |
| 60 to 69.99 | B+ |
| 50 to 59.99 | B |
| 40 to 49.99 | C |
| Below 40 | F |

A student is marked as `Fail` if any subject score is below 35; otherwise, the result is `Pass`.

## How to Run

1. Make sure Python is installed on your system.
2. Install the required libraries:

```bash
pip install pandas numpy
```

3. Open the project folder in Visual Studio Code or any terminal.
4. Run the script:

```bash
python main.py
```

5. The program will print the full student report and save the processed file as `student_performance_report.csv`.

## Output

When the script runs successfully, it generates:

- A terminal summary containing:
  - Student performance table
  - Class statistics
  - Pass/fail count
  - Subject-wise averages
  - Top 5 students
  - Attendance report
- A CSV file named `student_performance_report.csv`

## Example Summary

From the current dataset, the script reports:

- Total Students: 20
- Class Average: 72.35
- Highest Average: 95.0
- Lowest Average: 31.6
- Students Passed: 18
- Students Failed: 2

## Notes

- The project uses sample academic data for demonstration.
- The script assumes that the CSV columns remain consistent and correctly named.
- The pass rule is set to a minimum score of 35 in any subject.

## Future Improvements

- Add input validation for missing or invalid values
- Add department-wise filtering and reporting
- Include charts and visual analytics
- Export more detailed summaries in Excel or PDF format
- Add a graphical user interface (GUI)

## License

This project is intended for educational and learning purposes.
