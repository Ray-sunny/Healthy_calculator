from Healthy_calculator_BMI_BMR_TDEE import cal_bmr_test
import unittest

class BmrTestCase(unittest.TestCase):
    def test_cal_bmt(self):
        result_1 = cal_bmr_test(160,60,'female',24)
        result_2 = cal_bmr_test(188,90,'male',56)
        result_3 = cal_bmr_test(190,40,'male',7)
        result_4 = cal_bmr_test(140,70,'female',89)
        result_5 = cal_bmr_test(156,63,'female',30)
        self.assertEqual(1406.2,result_1)
        self.assertEqual(1858.2,result_2)
        self.assertEqual(1516.4,result_3)
        self.assertEqual(1160.7,result_4)
        self.assertEqual(1399.6,result_5)

if __name__ == '__main__':
    unittest.main()

