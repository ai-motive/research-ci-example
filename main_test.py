import unittest
import main


class MainTest(unittest.TestCase):
    def test_hellowrld(self):
        ret = main.helloworld('Test')
        self.assertEqual(ret, "Hello World! Chris!")

if __name__ == "__main__":
    unittest.main()