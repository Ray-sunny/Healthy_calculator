from Healthy_calculator_BMI_BMR_TDEE_2 import cal_bmi_test, comparing_BMI
import unittest

class BmiTestCase(unittest.TestCase):
    def test_cal_bmi(self):
        result_1 = cal_bmi_test(165,75)
        result_2 = cal_bmi_test(165, 50)
        result_3 = cal_bmi_test(180,70)
        result_4 = cal_bmi_test(160,90)
        result_5 = cal_bmi_test(160,80)
        self.assertEqual(27.5, result_1)
        self.assertEqual(18.4, result_2)
        self.assertEqual(21.6, result_3)
        self.assertEqual(35.2, result_4)
        self.assertEqual(31.2, result_5)

    def test_comparing_bmi(self):
        result_1 = comparing_BMI(18)
        result_2 = comparing_BMI(24)
        result_3 = comparing_BMI(27)
        result_4 = comparing_BMI(30)
        result_5 = comparing_BMI(35)
        result_6 = comparing_BMI(18.5)
        self.assertEqual('You are underweight', result_1)
        self.assertEqual('You are overweight', result_2)
        self.assertEqual('You are slight obesity', result_3)
        self.assertEqual('You are middle obesity', result_4)
        self.assertEqual('You are extreme obesity', result_5)
        self.assertEqual('You have healthy body weight', result_6)



if __name__ == '__main__':
    unittest.main()
