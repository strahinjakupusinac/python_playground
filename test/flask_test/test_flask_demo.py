# -*- coding: utf-8 -*-
'''
Created on Oct 31, 2013

@author: Strahinja
'''
import unittest
import src.flask_test.flask_demo_app
import json
import base64

class FlaskTestCase(unittest.TestCase):


    def make_headers(self, username, password):
        auth = base64.b64encode(username + ':' + password)
        return {'Content-Type':'application/json', 'Authorization':b'Basic ' + auth} 
    
    
    def setUp(self):
        src.flask_test.flask_demo_app.app.config['TESTING'] = True
        self.app = src.flask_test.flask_demo_app.app.test_client()
        pass


    def tearDown(self):
        pass


    def testAddName(self):
        nameToAdd = 'Pera'
        expectedResult = {'result':'ok'}
        response = self.app.put('/names', headers={'Content-Type':'application/json'}, data = json.dumps(nameToAdd))
        result = json.loads(response.data)
        self.assertEqual(expectedResult, result)
        expectedResult = {'names':['Pera']}
        result = json.loads(self.app.get('/names').data)
        self.assertEqual(expectedResult, result)


    def testForward(self):
        username = 'admin'
        password = 'admin'
        testJson = {'person':{'firstNam':'Strahinja', 'lastName':'Kupusinac', 'addresses':[u'Bulevar Jovana Dučića 39g, Novi Sad', u'ЈНА 65 Товаришево']}}
        print(testJson)
        headers = self.make_headers(username,password)
        response = self.app.post('/forward', headers=headers, data = json.dumps(testJson))
        self.assertEqual(200, response.status_code)
        resultJson = json.loads(response.data)
        self.assertEqual(testJson, resultJson)

            
if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
