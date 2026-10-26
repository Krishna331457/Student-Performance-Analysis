
import pandas as pd
import numpy as np

# Subjects used in the project

SUBJECTS = ["Python", "SQL", "Java", "CSS", "JavaScript"]


# 1. Load student dataset

def load_data():
    df = pd.read_csv("students.csv")
    return df


# 2. Calculate total and average marks

def calculate_marks(df):
    df["Total"] = df[SUBJECTS].sum(axis=1)
    df["Average"] = df[SUBJECTS].mean(axis=1).round(2)
    return df


# 3. Assign grade according to average marks

def assign_grade(average):
    if average >= 90:
        return "O"
    elif average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B+"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


# 4. Check pass or fail

def check_result(row):
    for subject in SUBJECTS:
        if row[subject] < 35:
            return "Fail"
    return "Pass"


# 5. Perform complete analysis

def analyze_data(df):

    # Apply grades and results

    df["Grade"] = df["Average"].apply(assign_grade)
    df["Result"] = df.apply(check_result, axis=1)

    print("\n===== STUDENT PERFORMANCE REPORT =====")
    print(df.to_string(index=False))

    # Class statistics using NumPy

    averages = df["Average"].to_numpy()

    print("\n===== CLASS STATISTICS =====")
    print("Total Students:", len(df))
    print("Class Average:", round(np.mean(averages), 2))
    print("Highest Student Average:", round(np.max(averages), 2))
    print("Lowest Student Average:", round(np.min(averages), 2))

    # Pass/fail statistics

    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()

    print("\n===== PASS / FAIL REPORT =====")
    print("Students Passed:", passed)
    print("Students Failed:", failed)

    # Subject-wise average

    print("\n===== SUBJECT-WISE AVERAGE =====")
    for subject in SUBJECTS:
        subject_average = np.mean(df[subject].to_numpy())
        print(subject, "Average:", round(subject_average, 2))

    # Top 5 students

    print("\n===== TOP 5 STUDENTS =====")
    top_students = df.nlargest(5, "Average")

    print(
        top_students[["Name", "Average", "Grade", "Result"]]
        .to_string(index=False)
    )

    # Attendance analysis

    print("\n===== ATTENDANCE REPORT =====")
    print(
        "Average Attendance:",
        round(np.mean(df["Attendance"].to_numpy()), 2),
        "%"
    )

    return df


# 6. Main function

def main():
    df = load_data()
    df = calculate_marks(df)
    df = analyze_data(df)

    # Save final report

    df.to_csv("student_performance_report.csv", index=False)

    print("\nReport saved as student_performance_report.csv")


# Run the project

if __name__ == "__main__":
    main()
