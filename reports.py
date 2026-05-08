# reports.py
# Developer C — Reporting & summaries
# Branch: feature/reports

from grades import get_average


def get_top_students(students: dict, grades: dict, n: int = 3) -> list:
    """
    Return the top n students with the highest average scores.

    - Returns a list of (student_id, name, average) tuples.
    - Sorted by average in descending order (highest first).
    - If n is greater than the number of students, return all of them.
    - Students with no grades have an average of 0.0.

    Args:
        students (dict): the students database
        grades (dict): the grades database
        n (int): number of top students to return (default 3)

    Returns:
        list[tuple]: list of (student_id, name, average) sorted descending
    """

    # Creation of tuples (unsorted)
    unsorted_list = []
    for k, v in students.items():
        student_id = k
        name = v.get("name")
        average = get_average(grades, student_id)
        unsorted_list.append((student_id, name, average))

    # Sort the unsorted list via "average" (3rd element of the tuple)
    sorted_list = sorted(unsorted_list, key = lambda student: student[2], reverse=True)

    # Return the "n" best students of the class
    if n >= (len(students)):
        return sorted_list
    else:
        return sorted_list[0:n]



def summarize_class(students: dict, grades: dict) -> tuple:
    """
    Return a summary of the whole class as a single tuple.

    The tuple must contain exactly 4 values in this order:
        (total_students, class_average, highest_average, lowest_average)

    - total_students (int): number of students in the database
    - class_average (float): average of all students' averages, rounded to 2 decimals
    - highest_average (float): the best individual average in the class
    - lowest_average (float): the worst individual average in the class

    - If there are no students, return (0, 0.0, 0.0, 0.0).

    Args:
        students (dict): the students database
        grades (dict): the grades database

    Returns:
        tuple: (total_students, class_average, highest_average, lowest_average)
"""

    # Initialisation
    total_students = len(students)
    averages = []
    class_average = 0.0
    highest_average = 0.0
    lowest_average = 0.0
    # Managing case "len(students) = 0 to avoid a DivisionByZero error.
    if len(students) == 0:
        return total_students, class_average, highest_average, lowest_average
    # Calculating students averages
    else:
        for student in students.keys():
            average = get_average(grades, student)
            averages.append(average)
    # Formating before return
    class_average = float( format(sum(averages)/len(averages), ".2f") )
    highest_average = max(averages)
    lowest_average = min(averages)
    return total_students, class_average, highest_average, lowest_average



def export_report(students: dict, grades: dict) -> str:
    """
    Generate and return a formatted text report as a single string.

    The report must follow this exact format:
    ─────────────────────────────────
    GRADEBOOK REPORT
    Total students: 3
    Class average:  75.33

    STUDENT DETAILS
    S001 | Alice Smith     | Avg:  85.00 | Subjects: English, Math, Science
    S002 | Bob Martin      | Avg:  62.50 | Subjects: Math, Science
    S003 | Carol White     | Avg:   0.00 | Subjects: none
    ─────────────────────────────────

    Rules:
    - Student names are left-aligned in a field of 16 characters.
    - Averages are right-aligned with 2 decimal places.
    - Subjects are listed in alphabetical order, comma-separated.
    - If a student has no grades, show "none" for subjects.
    - Use summarize_class() to get total_students and class_average.
    - Students are listed in alphabetical order by name.

    Args:
        students (dict): the students database
        grades (dict): the grades database

    Returns:
        str: the complete formatted report
    """

    # Initialisation
    report = ""

    # Header
    header = "─────────────────────────────────\n"
    header += "GRADEBOOK REPORT\n"
    header += f"Total students: {len(students)}\n"
    header += f"Class average:  {summarize_class(students, grades)[1]}\n"

    # Students details
    for matricule in students.keys():
        student_line

    return report

    raise NotImplementedError("export_report is not implemented yet.")
