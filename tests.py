import unittest
import io
from pathlib import Path
from main import word_count

class TestStringMethods(unittest.TestCase):
    def test_basic_file(self):
        local_filename = "./test_file1.txt"
        decoded_file = Path(local_filename).read_text()
        input_file = io.StringIO(decoded_file)
        expected_wc = {
            'this': 2, 
            'is': 1, 
            'a': 1, 
            'very': 1, 
            'basic': 1, 
            'file': 1, 
            'with': 1, 
            '1': 1, 
            'repeated': 1, 
            'word': 1}
        actual_wc = word_count(input_file)
        self.assertEqual(actual_wc, expected_wc)

    def test_harder_file(self):
        local_filename = "./test_file2.txt"
        decoded_file = Path(local_filename).read_text()
        input_file = io.StringIO(decoded_file)
        actual_wc = word_count(input_file)
        print(actual_wc)
        #self.assertEqual(actual_wc, expected_wc)

if __name__ == '__main__':
    unittest.main()
