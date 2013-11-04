# -*- coding: utf-8 -*-
'''
Created on Oct 31, 2013

@author: Strahinja
'''
import unittest
import src.flask_test.flask_demo_app
import json

class FlaskTestCase(unittest.TestCase):


    def setUp(self):
        src.flask_test.flask_demo_app.app.config['TESTING'] = True
        self.app = src.flask_test.flask_demo_app.app.test_client()
        pass


    def tearDown(self):
        pass


    def testAddName(self):
        nameToAdd = 'Pera'
        expectedResult = {'result':'ok'}
        result = json.loads(self.app.put('/names', headers={'Content-Type':'application/json'}, data = json.dumps(nameToAdd)).data)
        self.assertEqual(expectedResult, result)
        expectedResult = {'names':['Pera']}
        result = json.loads(self.app.get('/names').data)
        self.assertEqual(expectedResult, result)


    def testForward(self):
        testJson = {'person':{'firstNam':'Strahinja', 'lastName':'Kupusinac', 'addresses':[u'Bulevar Jovana Dučića 39g, Novi Sad', u'ЈНА 65 Товаришево']}}
        print(testJson)
        response = self.app.post('/forward', headers={'Content-Type':'application/json'}, data = json.dumps(testJson))
        self.assertEqual(200, response.status_code)
        resultJson = json.loads(response.data)
        self.assertEqual(testJson, resultJson)
            
if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()