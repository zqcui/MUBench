import unittest

from utils import command_line_util


class CommandLineUtilTest(unittest.TestCase):
    def setUp(self):
        self.parser = command_line_util.get_command_line_parser()

    def test_mode_check(self):
        result = self.parser.parse_args(['check'])
        self.assertEqual('check', result.mode)

    def test_mode_checkout(self):
        result = self.parser.parse_args(['checkout'])
        self.assertEqual('checkout', result.mode)

    def test_mode_mine_fails_without_miner(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['mine'])

    def test_mode_mine_with_miner(self):
        test_miner = 'dummy-miner'
        result = self.parser.parse_args(['mine', test_miner])
        self.assertEqual(test_miner, result.miner)

    def test_mode_evaluate_fails_without_detector(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['eval'])

    def test_mode_evaluate_with_detector(self):
        test_detector = 'dummy-detector'
        result = self.parser.parse_args(['eval', test_detector])
        self.assertEqual(test_detector, result.detector)

    def test_stops_on_invalid_mode(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['invalid'])

if __name__ == '__main__':
    unittest.main()
