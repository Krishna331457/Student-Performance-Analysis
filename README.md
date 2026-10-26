Student Performance Analytics System
Project Overview
The Student Performance Analytics System is a beginner-friendly Python
data-analysis project. It reads student records from a CSV file,
calculates total and average marks, assigns grades, checks pass/fail
status, summarizes class performance and attendance, and saves a
processed report.

Dataset note: The sample records used for this project are synthetic
demonstration data, not verified real college records.
Objectives
- Load student records from students.csv.
- Calculate total and average marks across five subjects.
- Assign grades and determine pass/fail status.
- Calculate class and subject-wise statistics.
- Identify the top three students by average marks.
- Calculate average attendance.
- Save the processed data to student_performance_report.csv.
Technologies Used
- Python --- program logic, functions, loops, and conditions.
- Pandas --- reading CSV files, working with tabular data, and
  exporting reports.
- NumPy --- numerical summaries such as mean, minimum, and
  maximum.
- CSV --- input dataset and output report.
- Visual Studio Code --- code editor used to develop and run the
  project.
Dataset Description
The input file is students.csv. It should include these columns:

  Column         Description
  Student_ID   Unique student identifier
  Name         Student name
  Department   Department name, e.g. CSE or IT
  Python       Python marks out of 100
  SQL          SQL marks out of 100
  Java         Java marks out of 100
  CSS          CSS marks out of 100
  JavaScript   JavaScript marks out of 100
  Attendance   Attendance percentage from 0 to 100

The program can process more student rows without code changes as long
as the column names and data format remain consistent. Use unique
student IDs and numeric marks.
Key Features
1. Calculates total marks across five subjects (maximum 500 if each
   subject is out of 100).
2. Calculates average marks across five subjects (maximum 100).
3. Assigns grades using these project rules:
   - 90 and above: O
   - 80 to below 90: A+
   - 70 to below 80: A
   - 60 to below 70: B+
   - 50 to below 60: B
   - 40 to below 50: C
   - Below 40: F
4. Returns Fail if any subject mark is below 35; otherwise returns
   Pass.
5. Displays total students, class average, highest student average, and
   lowest student average.
6. Calculates subject-wise average marks.
7. Displays the top three students by average marks.
8. Calculates average attendance.
9. Exports processed records to student_performance_report.csv.
Project Structure
student-performance-analytics/
├── main.py
├── students.csv
├── README.md
└── student_performance_report.csv  # generated when the program runs
How to Run
1. Keep main.py and students.csv in the same folder.
2. Use the Python environment in which Pandas and NumPy are available.
3. Open the folder in Visual Studio Code.
4. Open the terminal in that folder and run:
   python main.py
5. Review the report printed in the terminal.
6. Confirm that student_performance_report.csv is created or updated.
Output Files
- students.csv --- input student dataset.
- student_performance_report.csv --- processed dataset with Total,
  Average, Grade, and Result columns.
Limitations
- Required column names must match exactly.
- Marks and attendance should be numeric and within the expected
  range.
- The passing threshold of 35 per subject and grade bands are
  project-defined rules and may differ from a college's official
  policy.
- This version creates text and CSV reports; it does not implement
  machine learning or charts.
Future Improvements
- Validate missing or out-of-range marks.
- Add charts for subject-wise and class performance.
- Add department-wise filters.
- Allow data entry through a form.
- Compare performance across semesters.
Student Details
- Student Name: \(Krishna kumar Dubey)
- Course / Department: \(B.Tech CSE)
- Institution: \(Jagannath University, Jaipur)
