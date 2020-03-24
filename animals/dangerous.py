

class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Tiger', 'Lion', 'Wild Cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member )



class Birds:
    def __init__(self):
        '''Constructor of class'''
        #Create some member animals
        self.members = ['Lammergeier', 'Emu', 'Eagle']

    def printMembers(self):
        print('Printing members of the Birds class:')
        for member in self.members:
            print('\t%s' % member)



class Fish:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Puffer fish  ', 'Piranha', 'Jelly fish']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s' % member )









