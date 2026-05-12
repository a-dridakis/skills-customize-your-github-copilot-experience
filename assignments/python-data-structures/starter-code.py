"""
Python Data Structures Assignment - Starter Code

This starter code provides a foundation for managing student records
using Python's core data structures: lists, tuples, dictionaries, and sets.
"""

# =============================================================================
# TASK 1: Working with Lists and Tuples
# =============================================================================

def add_student(students, student_id, name, grade):
    """
    Add a new student record to the list.
    
    Args:
        students (list): List of student tuples
        student_id (int): Unique student identifier
        name (str): Student's name
        grade (float): Student's grade
    
    Returns:
        list: Updated student list
    """
    # TODO: Create a tuple for the student and add to list
    pass


def remove_student(students, student_id):
    """
    Remove a student from the list by ID.
    
    Args:
        students (list): List of student tuples
        student_id (int): ID of student to remove
    
    Returns:
        list: Updated student list
    """
    # TODO: Filter out the student with matching ID
    pass


def sort_by_grade(students, descending=False):
    """
    Sort students by grade.
    
    Args:
        students (list): List of student tuples
        descending (bool): If True, sort highest to lowest
    
    Returns:
        list: Sorted list of students
    """
    # TODO: Sort students by grade (index 2 of tuple)
    pass


def search_student(students, search_type='id', search_value=None):
    """
    Search for a student by ID or name.
    
    Args:
        students (list): List of student tuples
        search_type (str): 'id' or 'name'
        search_value: Value to search for
    
    Returns:
        tuple: Student tuple if found, None otherwise
    """
    # TODO: Search through list and return matching student
    pass


def display_students(students):
    """
    Display all students in a formatted table.
    
    Args:
        students (list): List of student tuples
    """
    # TODO: Print students in a nicely formatted table
    pass


# =============================================================================
# TASK 2: Using Dictionaries for Efficient Data Access
# =============================================================================

class StudentDatabase:
    """
    A student management system using dictionaries.
    """
    
    def __init__(self):
        """Initialize the student database."""
        # TODO: Create dictionary to store students (ID -> student info)
        # Student info should be a dictionary with: name, grade, email, phone, major
        pass
    
    def add_student(self, student_id, name, grade, email='', phone='', major=''):
        """
        Add a new student to the database.
        
        Args:
            student_id (int): Unique student ID
            name (str): Student's name
            grade (float): Student's grade
            email (str): Student's email
            phone (str): Student's phone
            major (str): Student's major
        """
        # TODO: Create student dictionary and add to database
        pass
    
    def remove_student(self, student_id):
        """
        Remove a student by ID.
        
        Args:
            student_id (int): ID of student to remove
        
        Returns:
            bool: True if removed, False if not found
        """
        # TODO: Delete student from database dictionary
        pass
    
    def update_student(self, student_id, **kwargs):
        """
        Update student information.
        
        Args:
            student_id (int): Student ID to update
            **kwargs: Fields to update (name, grade, email, phone, major)
        """
        # TODO: Update student fields
        pass
    
    def get_student(self, student_id):
        """
        Get student information by ID.
        
        Args:
            student_id (int): Student ID to retrieve
        
        Returns:
            dict: Student information or None
        """
        # TODO: Return student dictionary from database
        pass
    
    def calculate_statistics(self):
        """
        Calculate grade statistics.
        
        Returns:
            dict: Statistics including average, max, min grades
        """
        # TODO: Calculate average, highest, and lowest grades
        pass
    
    def get_students_by_grade_range(self, min_grade, max_grade):
        """
        Get all students within a grade range.
        
        Args:
            min_grade (float): Minimum grade
            max_grade (float): Maximum grade
        
        Returns:
            list: List of matching students
        """
        # TODO: Filter students by grade range
        pass
    
    def find_by_field(self, field, value):
        """
        Find students by any field (name, email, phone, etc.).
        
        Args:
            field (str): Field name to search
            value: Value to match
        
        Returns:
            list: List of matching students
        """
        # TODO: Search for matching students in any field
        pass


# =============================================================================
# TASK 3: Sets and Advanced Data Operations
# =============================================================================

class SchoolEnrollment:
    """
    Track student enrollment using sets for efficient operations.
    """
    
    def __init__(self):
        """Initialize enrollment tracking."""
        # TODO: Create dictionaries of sets for different classes/clubs
        # Example: {'Computer Science': set(), 'Mathematics': set()}
        pass
    
    def enroll_student(self, subject, student_id):
        """
        Enroll a student in a subject or club.
        
        Args:
            subject (str): Subject or club name
            student_id (int): Student ID
        """
        # TODO: Add student_id to the set for this subject
        pass
    
    def find_common_students(self, subject1, subject2):
        """
        Find students enrolled in both subjects.
        
        Args:
            subject1 (str): First subject
            subject2 (str): Second subject
        
        Returns:
            set: Students in both subjects (intersection)
        """
        # TODO: Return intersection of two subject sets
        pass
    
    def find_all_students(self, *subjects):
        """
        Find all students in any of the given subjects.
        
        Args:
            *subjects: Variable number of subject names
        
        Returns:
            set: All students in any subject (union)
        """
        # TODO: Return union of all subject sets
        pass
    
    def find_unique_students(self, subject):
        """
        Find students unique to a subject (not in any other).
        
        Args:
            subject (str): Subject name
        
        Returns:
            set: Students only in this subject
        """
        # TODO: Return students in subject but not in any other
        pass
    
    def generate_enrollment_report(self):
        """
        Generate a report of overlapping enrollments.
        
        Returns:
            dict: Report of subject overlaps
        """
        # TODO: Create a report showing which subjects share students
        pass


# =============================================================================
# Example usage
# =============================================================================

if __name__ == "__main__":
    # Task 1 Example: Using lists and tuples
    print("Task 1: Student List Management")
    print("-" * 40)
    students = []
    
    # TODO: Add some sample students and test functions
    
    print("\n" + "="*40 + "\n")
    
    # Task 2 Example: Using dictionaries
    print("Task 2: Dictionary-based Database")
    print("-" * 40)
    db = StudentDatabase()
    
    # TODO: Add students and test database functions
    
    print("\n" + "="*40 + "\n")
    
    # Task 3 Example: Using sets
    print("Task 3: Enrollment with Sets")
    print("-" * 40)
    enrollment = SchoolEnrollment()
    
    # TODO: Enroll students and test set operations
