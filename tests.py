import unittest
import io
from pathlib import Path
from main import word_count, input_file

class TestStringMethods(unittest.TestCase):
    def test_basic_file(self):
        local_filename = "./test_file1.txt"
        decoded_file = Path(local_filename).read_text()
        local_file = io.StringIO(decoded_file)
        wc = word_count(local_file)
        self.assertEqual(wc["this"], 2)
        self.assertEqual(wc["repeated"], 1)
        self.assertFalse("1" in wc)

    def test_harder_file(self):
        local_filename = "./test_file2.txt"
        decoded_file = Path(local_filename).read_text()
        local_file = io.StringIO(decoded_file)
        wc = word_count(local_file)
        self.assertEqual(wc["some"], 2)
        self.assertEqual(wc["case"], 2)
        self.assertEqual(wc["character"], 1)
        self.assertEqual(wc["im"], 1)
        self.assertFalse("2" in wc)

    def test_hardest_file(self):
        local_filename = "./test_file3.txt"
        decoded_file = Path(local_filename).read_text()
        local_file = io.StringIO(decoded_file)
        wc = word_count(local_file)
        self.assertEqual(wc["a"], 4)
        self.assertEqual(wc["case"], 3)
        self.assertEqual(wc["its"], 2)
        self.assertFalse("234" in wc)

    
    def test_provided_file(self):
        wc = word_count(input_file)
        self.assertEqual(wc["phishing"], 142)
        self.assertEqual(wc["spearphishing"], 3)
        self.assertEqual(wc["emails"], 20)

if __name__ == '__main__':
    unittest.main()
