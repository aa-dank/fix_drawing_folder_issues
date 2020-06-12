import unittest
import manual_f5_fix


class testManualF5(unittest.TestCase):

    def test_f5_test(self):
        z = manual_f5_fix.directory_obj(r"S:\Project Folders\Aaron Dankert\Test2\9400-001")
        y = z.f5_test()
        self.assertEqual(y, [False, False])


if __name__ == '__main__':
    unittest.main()

