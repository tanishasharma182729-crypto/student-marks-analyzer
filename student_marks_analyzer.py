"""
Project: Student Marks Analyzer using Python
Student: Tanisha Sharma
Course: Introduction to AI and Python Essentials

This beginner-friendly program analyzes marks for five subjects, calculates
the total and average, assigns a grade, and gives a rule-based study suggestion.

Note: This is a rule-based program inspired by simple decision systems. It is
not a machine-learning model and does not learn from data.
"""

def get_mark(subject_number):
    """Read and validate a mark from 0 to 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {subject_number} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def analyze_performance(average):
    """Return a grade and a rule-based recommendation."""
    if average >= 90:
        return "A+", "Excellent performance. Keep challenging yourself."
    elif average >= 80:
        return "A", "Very good work. Revise regularly to maintain your result."
    elif average >= 70:
        return "B", "Good performance. Practise the topics where you lost marks."
    elif average >= 60:
        return "C", "Fair performance. Make a weekly revision plan."
    elif average >= 40:
        return "D", "You passed the basic threshold. Practise more and ask for help."
    else:
        return "F", "Focus on fundamentals and make a step-by-step improvement plan."


def main():
    print("=" * 44)
    print("       STUDENT MARKS ANALYZER")
    print("=" * 44)

    name = input("Enter student name: ").strip()
    if not name:
        name = "Student"

    marks = []
    for subject_number in range(1, 6):
        marks.append(get_mark(subject_number))

    total = sum(marks)
    average = total / len(marks)
    grade, suggestion = analyze_performance(average)

    print("\n" + "-" * 44)
    print("               RESULT")
    print("-" * 44)
    print(f"Student name : {name}")
    print(f"Total marks  : {total:g} / 500")
    print(f"Average      : {average:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Suggestion   : {suggestion}")
    print("-" * 44)


if __name__ == "__main__":
    main()
