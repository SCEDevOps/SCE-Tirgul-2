from app.views import login, validateUser
import unittest
import nose


class name(unittest.TestCase):

    def test(self):
        invalid_login = self.app.post('login', data=dict(login='invalid', password='invalid'), follow_redirects=True)
        assert 'Invalid credentials' in invalid_login.data


if __name__ == '__main__':
    unittest.main()
