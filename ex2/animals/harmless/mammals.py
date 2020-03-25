

class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Horse', 'Dog', 'Mouse']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member )
