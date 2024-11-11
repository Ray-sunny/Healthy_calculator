from Healthy_calculator_BMI_BMR_TDEE_2 import cal_tdee_test
import unittest

class TdeeTestCase(unittest.TestCase):
    def test_cal_tdee(self):
        result_1 = cal_tdee_test(160, 60, 'female', 24, "1 - Sedentary, little to no exercise")
        result_2 = cal_tdee_test(188, 90, 'male', 56, "2 - Light exercise 1-3 days per week")
        result_3 = cal_tdee_test(190, 40, 'male', 7, "3 - Moderate exercise 3-5 days per week")
        result_4 = cal_tdee_test(140, 70, 'female', 89, "4 - Intense exercise 6-7 days per week")
        result_5 = cal_tdee_test(156, 63, 'female', 30, "5 - Physically demanding job or intense daily training")
        self.assertEqual(1687.44,result_1)
        self.assertEqual(2555.03,result_2)
        self.assertEqual(2350.42,result_3)
        self.assertEqual(2002.21,result_4)
        self.assertEqual(2659.24,result_5)

if __name__ == '__main__':
    unittest.main()