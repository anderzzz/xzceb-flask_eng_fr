import unittest
from translator import english2french, french2english

from ibm_cloud_sdk_core.api_exception import ApiException

class TestTranslator(unittest.TestCase):
    def test_english2frenchSimpleTranslation(self):
        self.assertEqual(english2french('Hello'), 'Bonjour')
        self.assertEqual(english2french('Bonjour'), 'Bonjour')

    def test_english2frenchNull(self):
        self.assertRaises(ValueError, english2french, None)
        self.assertRaises(ApiException, english2french, '')
        self.assertRaises(TypeError, english2french)

    def test_french2englishSimpleTranslation(self):
        self.assertEqual(french2english('Bonjour'), 'Hello')
        self.assertEqual(french2english('Hello'), 'Hello')

    def test_french2englishNull(self):
        self.assertRaises(ValueError, french2english, None)
        self.assertRaises(ApiException, french2english, '')
        self.assertRaises(TypeError, french2english)

if __name__ == '__main__':
    unittest.main()