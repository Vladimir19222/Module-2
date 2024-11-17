import unittest
import logging
from runner_and_tournament import Runner

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Тестовый бегун", -5)
            [runner.walk() for i in range(10)]
            self.assertEqual(runner.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            athlete = Runner(6)
            athlete.name = athlete.name + ''
            [athlete.run() for i in range(10)]
            self.assertEqual(athlete.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == '__main__':
    unittest.main()
