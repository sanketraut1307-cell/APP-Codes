# Decorator to print a heading before and after the report
def report_header(func):
    def wrapper(*args, **kwargs):
        # Wrapper function accepts any number of arguments
        print("=" * 40)
        print(" STUDENT REPORT")
        print("=" * 40)

        # Call the original function
        func(*args, **kwargs)

        # Print ending line
        print("=" * 40)

    return wrapper


class Report:
    # Class variable (shared by all objects)
    college = "ABC Engineering College"

    # Constructor to initialize student details
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Class method to update the college name
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic method to display object information
    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    # Decorator used to add a report header
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)

        # Check whether the student has passed or failed
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")


# Create first student object
student1 = Report("Rahul", 101, 85)
student1.display_report()

print()

# Change the college name for all students
Report.change_college("XYZ Institute of Technology")

# Create second student object
student2 = Report("Priya", 102, 35)
student2.display_report()

#Output - 
# ========================================
#  STUDENT REPORT
# ========================================
# College : ABC Engineering College
# Name : Rahul
# Roll No : 101
# Marks : 85
# Result : PASS
# ========================================

# ========================================
#  STUDENT REPORT
# ========================================
# College : XYZ Institute of Technology
# Name : Priya
# Roll No : 102
# Marks : 35
# Result : FAIL
# ========================================
