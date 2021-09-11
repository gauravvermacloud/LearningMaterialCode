import unittest
import Class_Code


class unit_test(unittest.TestCase):
    def setUp(self):
        print("setting up")

    def tearDown(self):
        print("Tearing down")

    def test_function_factorial_0(self):
        self.assertEqual(Class_Code.my_fact().fact(0), 1)

    def test_function_factorial_1(self):
        self.assertEqual(Class_Code.my_fact().fact(1), 1)

    def test_function_factorial_5(self):
        self.assertEqual(Class_Code.my_fact().fact(5), 120)

    def test_function_factorial_with_minus_1(self):
        with self.assertRaises(ValueError):
            Class_Code.my_fact().fact(-1)


if __name__ == "__main__":
    unittest.main()
