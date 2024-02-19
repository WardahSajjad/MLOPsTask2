import pytest
from main import StudentsInMLOps

@pytest.fixture
def student_class():
    return StudentsInMLOps()

def test_initial_strength(student_class):
    assert student_class.getTotalStrength() == 0

def test_enroll_students(student_class):
    student_class.enrollStudents(5)
    assert student_class.getTotalStrength() == 5

def test_drop_students(student_class):
    student_class.enrollStudents(10)
    student_class.dropStudents(3)
    assert student_class.getTotalStrength() == 7

def test_drop_more_than_enrolled(student_class):
    student_class.enrollStudents(5)
    student_class.dropStudents(10)
    assert student_class.getTotalStrength() == 0

def test_class_name(student_class):
    assert student_class.getClassName() == "StudentsInMLOps"
