import unittest, logging
from Function import is_prime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PrimesTestCase(unittest.TestCase):
    """Tests for `Function.py`."""

    def test_is_five_prime(self):
        logger.info("\n************** Is 5 prime ******************")

        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()