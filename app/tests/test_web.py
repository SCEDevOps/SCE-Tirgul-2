import unittest
import nose

from app.views import validateUser


class testTry(unittest.TestCase):
    def checkAllDetails(self):
        self.assertFalse(validateUser("lilo","siksik",""))

if __name__ == '__main__':
    unittest.main()