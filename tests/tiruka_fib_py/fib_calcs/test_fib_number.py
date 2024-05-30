from unittest import main, TestCase
from tiruka_fib_py.fib_calcs.fib_number import rec_fibonacci_numbers


class RecFibNumberTest(TestCase):
    def test_zero(self):
        self.assertEqual(0, rec_fibonacci_numbers(0))

    def test_negative(self):
        self.assertIsNone(rec_fibonacci_numbers(-1))

    def test_one(self):
        self.assertEqual(1, rec_fibonacci_numbers(1))

    def test_two(self):
        self.assertEqual(1, rec_fibonacci_numbers(2))

    def test_twenty(self):
        self.assertEqual(6765, rec_fibonacci_numbers(20))


if __name__ == "__main__":
    main()
