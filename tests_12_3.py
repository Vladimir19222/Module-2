import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("Тестовый бегун")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        summ2 = Runner('summ2')
        [summ2.run() for i in range(10)]
        self.assertEqual(summ2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        summ3, summ4 = Runner('summ3'), Runner('summ4')
        [(summ3.walk(), summ4.run()) for i in range(10)]
        self.assertNotEqual(summ3.distance, summ4.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    def setUp(self):
        self.athlete1 = Runner('Усэйн', 10)
        self.athlete2 = Runner('Андрей', 9)
        self.athlete3 = Runner('Ник', 5)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        t1 = Tournament(90, self.athlete1, self.athlete3)
        t1_res = {keys: str(value) for keys, value in t1.start().items()}
        self.all_results[1] = t1_res
        self.assertTrue(t1)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        t2 = Tournament(90, self.athlete2, self.athlete3)
        t2_res = {keys: str(value) for keys, value in t2.start().items()}
        self.all_results[2] = t2_res
        self.assertTrue(t2)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        t3 = Tournament(90, self.athlete1, self.athlete2, self.athlete3)
        t3_res = {keys: str(value) for keys, value in t3.start().items()}
        self.all_results[3] = t3_res
        self.assertTrue(t3)


if __name__ == '__main__':
    unittest.main()