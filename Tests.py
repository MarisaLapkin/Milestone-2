import unittest
from Class_Setup import Housing_Data
from Housing_Data import Central_Cal_Data
import main

class MyTestCase(unittest.TestCase):
    # def test_student_population_total_1(self):
    #     input1 = Central_Cal_Data
    #     input2 = 2022
    #     result = main.student_population_total(input1, input2)
    #     expected =
    #     self.assertEqual(result,expected)

    def test_student_population_total_1(self):
        input1 = Central_Cal_Data
        input2 = 2019
        result = main.student_population_total(input1, input2)
        expected = -1
        self.assertEqual(result, expected)


#write your tests, I will write my tests later because I need you to complete the Housing_data before I do

if __name__ == '__main__':
    unittest.main()
