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

    def test_student_percentage_1(self):
        input1 = Central_Cal_Data
        input2 = "Cal Poly San Luis Obispo"
        input3 = 2022
        result = main.student_percentage(input1, input2, input3)
        expected = 44.24, "%"
        self.assertEqual(result, expected)

    def test_homesless_percentage_1(self):
        input1 = Central_Cal_Data
        input2 = "San Jose State"
        result = main.homeless_percentage(input1, input2)
        expected = 0.97
        self.assertEqual(result, expected)

    def test_csu_homeless_1(self):
        input1 = Central_Cal_Data
        input2 = 1
        result = main.csu_homelessness(input1, input2)
        expected = "The universities that have a higher percentage of homeless than 1% include ['Cal Poly San Luis Obispo', 'CSU Monterey Bay']"
        self.assertEqual(result, expected)

    def test_csu_lowest_housing_price_1(self):
        input1 = Central_Cal_Data
        result = main.csu_lowest_housing_price(input1)
        expected = "The school with the lowest average rent is CSU Bakersfield at $1222 per month"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
