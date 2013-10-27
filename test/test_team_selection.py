'''
Created on Sep 29, 2013

@author: Strahinja
'''
import unittest
import src.team_selection
from src.team_selection import TeamSelection
from src import team_selection


class Test(unittest.TestCase):


    def testCase1(self):
        ts = TeamSelection()
        preference1 = [1, 2, 3, 4]
        preference2 = [1, 2, 3, 4]
        expectedResult = [1, 2, 1, 2]
        actualResult = ts.simulate(preference1, preference2)
        print(actualResult)
        self.assertEqual(actualResult, expectedResult, actualResult)

    def testCase2(self):
        ts = TeamSelection()
        preference1 = [3, 2, 1]
        preference2 = [1, 3, 2]
        expectedResult = [2, 1, 1]
        actualResult = ts.simulate(preference1, preference2)
        print(actualResult)
        self.assertEqual(actualResult, expectedResult, actualResult)


    def testCase3(self):
        ts = TeamSelection()
        preference1 = [6, 1, 5, 2, 3, 4]
        preference2 = [1, 6, 3, 4, 5, 2]
        expectedResult = [2, 1, 2, 2, 1, 1]
        actualResult = ts.simulate(preference1, preference2)
        print(actualResult)
        self.assertEqual(actualResult, expectedResult, actualResult)

    def testCase4(self):
        ts = TeamSelection()
        preference1 = [8, 7, 1, 2, 4, 5, 6, 3, 9]
        preference2 = [7, 2, 4, 8, 1, 5, 9, 6, 3]
        expectedResult = [1, 2, 1, 1, 2, 1, 2, 1, 2]
        actualResult = ts.simulate(preference1, preference2)
        print(actualResult)
        self.assertEqual(actualResult, expectedResult, actualResult)
    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
