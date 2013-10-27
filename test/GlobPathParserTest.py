'''
Created on Oct 3, 2013

@author: Strahinja
'''
import unittest
from src.GlobPathParser import GlobPathParser

class Test(unittest.TestCase):

    
    
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCase1(self):
        testPath = "/adtech/rawlogs/{{20121015}/{{22},{23}},{20121016}/{{00},{01},{02},{03},{04},{05},{06},{07},{08},{09},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21}}}/{*}.avro"
        
        leftBrackets = []
        rightBrackets = []
        slashes = []
        subSlashes = []
        i = 0
        for char in testPath:
            if char == "{":
                leftBrackets.append(i)
            elif char == "}":
                rightBrackets.append(i)
            elif char == "/":
                if len(leftBrackets) == len(rightBrackets):
                    slashes.append(i)
                else:
                    subSlashes.append(i)
            i += 1    
        print(slashes)       
        print(subSlashes)
        print(leftBrackets)
        print(rightBrackets)
        #gpp = GlobPathParser()
        #print(gpp.getSubPaths(testPath))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCase1']
    unittest.main()