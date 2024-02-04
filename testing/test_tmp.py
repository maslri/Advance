import unittest
import tmp

class TestFirst(unittest.TestCase) :
    def test_add(self) :
        result = tmp.add(15, 9)
        self.assertEqual(result, 24)
    
    def test_divide(self) :
        # self.assertRaises(ValueError, tmp.divide, 2, 0)
        with self.assertRaises(ValueError) :
            tmp.divide(2, 0)

    def test_init_pop(self) :
        result = tmp.init_pop(4, 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        cells = [True if len(i) == 4 else False for i in result]
        self.assertTrue(all(cells))

if __name__ == "__main__" :
    unittest.main()