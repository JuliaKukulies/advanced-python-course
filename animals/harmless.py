

class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Horse', 'Dog', 'Mouse']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member )



class Birds:
    def __init__(self):
        '''Constructor of class'''
        #Create some member animals
        self.members = ['Owl', 'Hummingbird', 'Parrot']

    def printMembers(self):
        print('Printing members of the Birds class:')
        for member in self.members:
            print('\t%s' % member)



class Fish:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Gold fish  ', 'Guppy', 'Blue fish']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s' % member )









