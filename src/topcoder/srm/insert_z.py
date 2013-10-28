'''
Created on Oct 26, 2013

@author: Strahinja
'''

class InsertZ(object):
    '''
    classdocs
    '''
  
    
    def __init__(self):
        '''
        Constructohr
        '''

    
    def CanTransfor(self, init, goal):
        if goal.replace('z','') == init.replace('z',''):
            return "Yes"
        else:
            return "No"
