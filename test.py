#!/usr/bin/env python3
import unittest
from main import rgb_to_hex, rgb_to_cmyk

# Test Suite
class TestRgbToHex(unittest.TestCase):
    def test_valid_rgb(self):
        self.assertEqual(rgb_to_hex(arguments=[0, 255, 99, 71]), "#FF6347")
        self.assertEqual(rgb_to_hex(arguments=[0, 0, 0, 0]), "#000000")
        self.assertEqual(rgb_to_hex(arguments=[0, 255, 255, 255]), "#FFFFFF")

    # Edge Cases
    def test_edge_cases(self):
        self.assertEqual(rgb_to_hex(arguments=[0, 0, 255, 0]), "#00FF00")
        self.assertEqual(rgb_to_hex(arguments=[0, 255, 0, 255]), "#FF00FF")

    def test_invalid_rgb(self):
        self.assertEqual(rgb_to_hex(arguments=[0, -1, 0, 0]), 'RGB values must be between 0 and 255.')
        self.assertEqual(rgb_to_hex(arguments=[0, 0, -1, 0]), 'RGB values must be between 0 and 255.')
        self.assertEqual(rgb_to_hex(arguments=[0, 0, 0, -1]), 'RGB values must be between 0 and 255.')
        self.assertEqual(rgb_to_hex(arguments=[0, 256, 0, 0]), 'RGB values must be between 0 and 255.')
        self.assertEqual(rgb_to_hex(arguments=[0, 0, 256, 0]), 'RGB values must be between 0 and 255.')
        self.assertEqual(rgb_to_hex(arguments=[0, 0, 0, 256]), 'RGB values must be between 0 and 255.')

    def test_invalid_type(self):
        self.assertEqual(rgb_to_hex(arguments=[0, "a", 0, 0]), 'Invalid input. Please enter integers for RGB values.')
        self.assertEqual(rgb_to_hex(arguments=[0, 0, "b", 0]), 'Invalid input. Please enter integers for RGB values.')
        self.assertEqual(rgb_to_hex(arguments=[0, 0, 0, "c"]), 'Invalid input. Please enter integers for RGB values.')
        self.assertEqual(rgb_to_hex(arguments=[0, 255.0, 0, 0]), 'Invalid input. Please enter integers for RGB values.')

# To run the test
if __name__ == '__main__':
    unittest.main()
