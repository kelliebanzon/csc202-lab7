import unittest
from hash_table_chaining import *

class TestStack(unittest.TestCase):

    def test_empty_hash_table(self):
        self.assertEqual(empty_hash_table(), HashTable())


if __name__ == "__main__":
    unittest.main()