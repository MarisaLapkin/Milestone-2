import unittest
from Class_Setup import Housing_Data
from Housing_Data import Central_Cal_Data
import main

class MyTestCase(unittest.TestCase):
    def test_student_population_total_1(self): #Marisa
        input1 = Central_Cal_Data
        input2 = 2022
        result = main.student_population_total(input1, input2)
        expected = 186585
        self.assertEqual(result,expected)

    def test_student_population_total_2(self):#Marisa
        input1 = Central_Cal_Data
        input2 = 2019
        result = main.student_population_total(input1, input2)
        expected = -1
        self.assertEqual(result, expected)

    def test_housing_averages_total(self):#Marisa
        input = Central_Cal_Data
        result = main.housing_averages_total(input)
        expected = {'Average Rent':1951.91, 'Average Size':646.27}
        self.assertEqual(result,expected)

    def test_price_per_square_foot(self):#Marisa
        input1 = Central_Cal_Data
        input2 = 'Cal Poly San Luis Obispo'
        result = main.price_per_square_foot(input1, input2)
        expected = 3.22
        self.assertEqual(result, expected)

    def test_price_per_foot_lt(self):#Marisa
        input1 = Central_Cal_Data
        input2 = 3.0
        result = main.price_per_foot_lt(input1, input2)
        expected = ['CSU Bakersfield','Fresno State','CSU Stanislaus','CSU East Bay','Sacramento State']
        self.assertEqual(result, expected)

    def test_price_per_foot_gt(self):#Marisa
        input1= Central_Cal_Data
        input2 = 3.0
        result = main.price_per_foot_gt(input1, input2)
        expected = ['Cal Poly San Luis Obispo','San Jose State','San Fransisco State','CSU Monterey Bay','Cal Poly Maritime','Sonoma State']
        self.assertEqual(result, expected)

    def test_percent_students_oncampus(self):#Marisa
        input1 = Central_Cal_Data
        input2 = 'Cal Poly San Luis Obispo'
        input3 = 2022
        result = main.percent_students_oncampus(input1, input2, input3)
        expected = 40.28
        self.assertEqual(result, expected)

    def test_homeless_by_average_price(self):#Marisa
        input1 = Central_Cal_Data
        input2 = 2000
        result = main.homelessness_by_average_price(input1, input2)
        expected = {'above $2000':[['San Jose State',0.97],['San Fransisco State',.97],['CSU Monterey Bay',9.32],['Cal Poly Maritime',5.11],['Sonoma State',6.57]],'below $2000':[['Cal Poly San Luis Obispo', 2.98],['CSU Bakersfield',.32],['Fresno State',.46],['CSU Stanislaus',2.64],['CSU East Bay',.73],['Sacramento State',1.04]],'price is $2000':[]}
        self.assertEqual(result, expected)

###################################################

    def test_student_percentage_1(self):#Martin
        input1 = Central_Cal_Data
        input2 = "Cal Poly San Luis Obispo"
        input3 = 2022
        result = main.student_percentage(input1, input2, input3)
        expected = 44.24, "%"
        self.assertEqual(result, expected)

    def test_homesless_percentage_1(self):#Martin
        input1 = Central_Cal_Data
        input2 = "San Jose State"
        result = main.homeless_percentage(input1, input2)
        expected = 0.97
        self.assertEqual(result, expected)

    def test_csu_homeless_1(self):#Martin
        input1 = Central_Cal_Data
        input2 = 1
        result = main.csu_homelessness(input1, input2)
        expected = "The universities that have a higher percentage of homeless than 1% include ['Cal Poly San Luis Obispo', 'CSU Monterey Bay', 'CSU Stanislaus', 'Cal Poly Maritime', 'Sonoma State', 'Sacramento State']"
        self.assertEqual(result, expected)

    def test_csu_lowest_housing_price_1(self):#Martin
        input1 = Central_Cal_Data
        result = main.csu_lowest_housing_price(input1)
        expected = "The school with the lowest average rent is CSU Bakersfield at $1222 per month"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
