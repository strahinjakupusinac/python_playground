'''
Created on Sep 29, 2013

@author: Strahinja
'''

class TeamSelection:
    def simulate(self, preference1, preference2):
        result = [0]*len(preference1)
        while preference1 != [] and preference2 != []:
            result[preference1[0]-1] = 1
            preference2.remove(preference1[0])
            preference1.pop(0)
            if preference2 != []:
                result[preference2[0]-1] = 2
                preference1.remove(preference2[0])
                preference2.pop(0)
            
        return result
