import unittest
from calc import add

class TestCalc(unittest.TestCase):
  def test_add():
    assertEqual(add(4,1), 5)

if __name__ == "__main__":
  unittest.main()
