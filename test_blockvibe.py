# test_blockvibe.py
"""
Tests for BlockVibe module.
"""

import unittest
from blockvibe import BlockVibe

class TestBlockVibe(unittest.TestCase):
    """Test cases for BlockVibe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockVibe()
        self.assertIsInstance(instance, BlockVibe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockVibe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
