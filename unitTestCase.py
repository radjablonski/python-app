import unittest

# python3 -m unittest -v unitTestCase.py
# python3 -m pytest -v unitTestCase.py 
# python3 unitTestCase.py 

class UnitTestCase(unittest.TestCase):

    #this will be called only once at the beggining of the process
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')

    #this will be called only once at the End of the process
    @classmethod
    def setDownClass(cls):
        print('teardownClass\n')

    #this will be called every time at the beggining of test method is called (for ever unittest case)
    def setUp(self):
        print('setup\n')

    #this will be called every time at the end of test method is called (for ever unittest case)
    def tearDown(self):
        print('tearDown\n')
    
    #unittest case #1
    def test_data(self):
        print('test_data unittest case #1\n')


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    
if __name__ == '__main__':
    unittest.main()