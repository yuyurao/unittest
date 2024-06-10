import unittest
from slam import SLAM

class TestSLAM(unittest.TestCase):
    def setUp(self):
        self.slam = SLAM()

    def test_initial_position(self):
        self.assertEqual(self.slam.get_position(), (0, 0))

    def test_update_position(self):
        self.slam.update_position((1, 2))
        self.assertEqual(self.slam.get_position(), (1, 2))

    def test_map_update(self):
        self.slam.update_position((1, 2))
        self.slam.update_position((2, 2))
        expected_map = {(0, 0), (1, 2), (2, 2)}
        self.assertEqual(self.slam.get_map(), expected_map)

if __name__ == '__main__':
    unittest.main()
