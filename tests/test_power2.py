import unittest
from power import power, time


class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3

        self.assertEqual(power(base, exp), 8)
        # エラーになるだろう条件を書く
        with self.assertRaises(TypeError):
            power(3, 2)

    def test_times(self):
        num1 = 2
        num2 = 3
        self.assertEqual(time(num1, num2), 6)


if __name__ == "__main__":
    unittest.main()  # インスタンスを作成している
