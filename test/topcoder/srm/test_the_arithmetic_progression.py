'''
Created on Oct 26, 2013

@author: Strahinja
'''
import unittest
from src.topcoder.srm.the_arithmetic_progression import TheArithmeticProgression 

class Test(unittest.TestCase):


    def setUp(self):
        self.ap = TheArithmeticProgression()
        pass


    def tearDown(self):
        pass


    def testCase1(self):
        a,b,c = 0,1,2
        expectedChange = 0.0
        change = self.ap.minimumChange(a,b,c)
        self.assertEqual(change, expectedChange)

    def testCase2(self):
        a,b,c = 0,2,1
        expectedChange = 1.5
        change = self.ap.minimumChange(a,b,c)
        self.assertEqual(change, expectedChange)

    def testCase3(self):
        a,b,c = 3,2,1
        expectedChange = 0.0
        change = self.ap.minimumChange(a,b,c)
        self.assertEqual(change, expectedChange)
        
    def testCase4(self):
        a,b,c = 4,4,8
        expectedChange = 2.0
        change = self.ap.minimumChange(a,b,c)
        self.assertEqual(change, expectedChange)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()