import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        summ1 = Runner('summ1')
        [summ1.walk() for i in range(10)]
        self.assertEqual(summ1.distance, 50)

    def test_run(self):
        summ2 = Runner('summ2')
        [summ2.run() for i in range(10)]
        self.assertEqual(summ2.distance, 100)

    def test_challenge(self):
        summ3, summ4 = Runner('summ3'), Runner('summ4')
        [(summ3.walk(), summ4.run()) for i in range(10)]
        self.assertNotEqual(summ3.distance, summ4.distance)


if __name__ == "__main__":
    unittest.main()
