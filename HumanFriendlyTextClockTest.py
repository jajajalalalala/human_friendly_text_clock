import unittest
import HumanFriendlyTextClock as clock


class TestSum(unittest.TestCase):

    def test_num_to_words(self):
        self.assertEqual(clock.num_to_words(0), "twelve", "Should be twelve")
        self.assertEqual(clock.num_to_words(1), "one", "Should be one")
        self.assertEqual(clock.num_to_words(21), "twenty one", "Should be twenty one")
        self.assertEqual(clock.num_to_words(12), "twelve", "Should be twenty twelve")
        self.assertEqual(clock.num_to_words(30), "half", "Should be half")

    def test_get_hour_min(self):
        self.assertEqual(clock.get_hour_min("12:30"), ("12:30", 12, 30))
        self.assertEqual(clock.get_hour_min("12:00"), ("12:00", 12, 00))
        self.assertEqual(clock.get_hour_min("1:30"), ("1:30", 1, 30))
        self.assertEqual(clock.get_hour_min("02:30"), ("02:30", 2, 30))
        self.assertEqual(clock.get_hour_min("0:00"), ("0:00", 0, 0))
        self.assertEqual(clock.get_hour_min("7:00"), ("7:00", 7, 0))

    def test_get_human_friendly_text(self):
        self.assertEqual(clock.get_human_friendly_text("1:00"), "1:00 One o'clock")
        self.assertEqual(clock.get_human_friendly_text("2:00"), "2:00 Two o'clock")
        self.assertEqual(clock.get_human_friendly_text("13:00"), "13:00 One o'clock")
        self.assertEqual(clock.get_human_friendly_text("13:05"), "13:05 Five past one")
        self.assertEqual(clock.get_human_friendly_text("13:10"), "13:10 Ten past one")
        self.assertEqual(clock.get_human_friendly_text("13:25"), "13:25 Twenty five past one")
        self.assertEqual(clock.get_human_friendly_text("13:30"), "13:30 Half past one")
        self.assertEqual(clock.get_human_friendly_text("13:35"), "13:35 Twenty five to two")
        self.assertEqual(clock.get_human_friendly_text("13:55"), "13:55 Five to two")
        self.assertEqual(clock.get_human_friendly_text("13:30"), "13:30 Half past one")
        self.assertEqual(clock.get_human_friendly_text("00:00"), "00:00 Twelve o'clock")

    # def test_sum(self):
    #     self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    #
    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
