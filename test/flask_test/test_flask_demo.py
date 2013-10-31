'''
Created on Oct 31, 2013

@author: Strahinja
'''
import unittest
import src.flask_test.flask_demo_app

class FlaskTestCase(unittest.TestCase):


    def setUp(self):
        src.flask_test.flask_demo_app.app.config['TESTING'] = True
        self.app = src.flask_test.flask_demo_app.app.test_client()
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()