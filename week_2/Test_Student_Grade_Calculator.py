import unittest

from Student_Grade_Calculator import get_grade_info

class TestGradeCalculator(unittest.TestCase):

    def test_grade_A(self):
        grade , msg = get_grade_info(95)
        self.assertEqual(grade,"A")
    
    def test_grade_B(self):
        grade ,msg = get_grade_info(85)
        self.assertEqual(grade,("B"))

    def test_grade_E(self):
        grade ,msg = get_grade_info(40)
        self.assertEqual(grade,"E")

    def test_boundary(self):
        grade ,msg = get_grade_info(90)
        self.assertEqual(grade,"A")
if __name__ == "__main__":
    unittest.main()