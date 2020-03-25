


class Birds:
    def __init__(self):
        '''Constructor of class'''
        #Create some member animals
        self.members = ['Lammergeier', 'Emu', 'Eagle']

    def printMembers(self):
        print('Printing members of the Birds class:')
        for member in self.members:
            print('\t%s' % member)

