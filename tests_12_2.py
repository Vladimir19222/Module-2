import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        cls.all_results = [value for keys, value in cls.all_results.items()]
        for i, value in enumerate(cls.all_results):
            print(value)

    def setUp(self):
        self.athlete1 = Runner('Усэйн', 10)
        self.athlete2 = Runner('Андрей', 9)
        self.athlete3 = Runner('Ник', 5)

    def test_1(self):
        t1 = Tournament(90, self.athlete1, self.athlete3)
        t1_res = {keys: str(value) for keys, value in t1.start().items()}
        self.all_results[1] = t1_res
        self.assertTrue(t1_res[1], 'Ник')

    def test_2(self):
        t2 = Tournament(90, self.athlete2, self.athlete3)
        t2_res = {keys: str(value) for keys, value in t2.start().items()}
        self.all_results[2] = t2_res
        self.assertTrue(t2_res[2], 'Ник')

    def test_3(self):
        t3 = Tournament(90, self.athlete1, self.athlete2, self.athlete3)
        t3_res = {keys: str(value) for keys, value in t3.start().items()}
        self.all_results[3] = t3_res
        self.assertTrue(t3_res[3], 'Ник')


if __name__ == "__main__":
    unittest.main()
