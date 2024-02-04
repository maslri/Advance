import unittest
from student import Student

class TestFirst(unittest.TestCase) :

    @classmethod
    def setUpClass(cls) :
        pass
    
    @classmethod
    def tearDownClass(cls) :
        pass

    def setUp(self) :
        self.std1 = Student("a", "b", 0.0)
        self.std2 = Student("c", "d", 0.0)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_mail(self) :
        self.assertEqual(self.std1.mail(), "a.b@gmail.com")
        self.assertEqual(self.std2.mail(), "c.d@gmail.com")
    
    def test_full_name(self) :
        self.assertEqual(self.std1.full_name(), "a b")
        self.assertEqual(self.std2.full_name(), "c d")

if __name__ == "__main__" :
    unittest.main()
    