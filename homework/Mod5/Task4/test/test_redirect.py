import unittest
from contextlib import redirect_stdout, redirect_stderr
import io
import sys
from Mod5.Task4.redirect import redirect


class TestRedirect(unittest.TestCase):
    def test_redirect_stdout(self):
        new_stdout = io.StringIO()
        with redirect(stdout=new_stdout):
            print("Hello stdout.txt")
        self.assertEqual(new_stdout.getvalue(), "Hello stdout.txt\n")

    def test_redirect_stderr(self):
        new_stderr = io.StringIO()
        with redirect(stderr=new_stderr):
            print("Hello stderr.txt", file=sys.stderr)
        self.assertEqual(new_stderr.getvalue(), "Hello stderr.txt\n")

    def test_no_redirect(self):
        with redirect():
            print("This should go to standard stdout")
        self.assertTrue(True)  # Простая проверка, что код выполнен


if __name__ == '__main__':
    unittest.main()