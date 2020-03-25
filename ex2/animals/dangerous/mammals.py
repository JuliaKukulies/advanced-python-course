
class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Tiger', 'Lion', 'Wild Cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member )

