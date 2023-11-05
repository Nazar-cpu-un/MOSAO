import unittest
import maximize


class TestMain(unittest.TestCase):

    def test_f(self):
        self.assertEqual(maximize.f(0), 0, "func. returns incorrect result!")

    def test_maximize(self):
        self.assertGreater(maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[1], 0, "At least, one iteration must be processed!")
        self.assertGreaterEqual(maximize.f(maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[0]), maximize.f((maximize.a + maximize.b) / 2), "Greater value can be found in the scopes!")
        self.assertLessEqual(maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[0], maximize.b)
        self.assertGreaterEqual(maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[0], maximize.a)


if __name__ == '__main__':
    unittest.main()
