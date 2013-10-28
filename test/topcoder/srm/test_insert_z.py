'''
Created on Oct 26, 2013

@author: Strahinja
'''
import unittest
from src.topcoder.srm.insert_z import InsertZ

class TestInsertZ(unittest.TestCase):


    def setUp(self):
        self.iz = InsertZ()


    def tearDown(self):
        pass


    def testCase1(self):
        init = "fox"
        goal = "fozx"
        expectedResult = "Yes"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)


    def testCase2(self):
        init = "foon"
        goal = "foon"
        expectedResult = "Yes"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)


    def testCase3(self):
        init = "codecentric"
        goal = "zodezentriz"
        expectedResult = "No"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)
        
        
    def testCase4(self):
        init = "aaaaaaaaaa"
        goal = "a"
        expectedResult = "No"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)
        

    def testCase5(self):
        init = "mvixrdnrpxowkasufnvxaq"
        goal = "mvizzxzzzrdzznzrpxozzwzzkazzzszzuzzfnvxzzzazzq"
        expectedResult = "Yes"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)
        

    def testCase6(self):
        init = "opdlfmvuicjsierjowdvnx"
        goal = "zzopzdlfmvzuicjzzsizzeijzowvznxzz"
        expectedResult = "No"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)
        
    def testCase7(self):
        init = "pazaz"
        goal = "pazazz"
        expectedResult = "Yes"
        self.assertEqual(self.iz.CanTransfor(init, goal), expectedResult)
                   
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
