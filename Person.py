class Person:
    counter = 0

    def __init__(self, attr_array):
        self.id = self.counter
        self.name = attr_array[1]
        self.age = attr_array[2]
        self.rating = attr_array[3]


    def get_attr_at_index(self, index):
        return [self.id, self.name, self.age, self.rating][index]

    def __str__(self):
        return 'ID:{}, Name:{}, Age:{}, Rating:{}'.format(self.id,self.name,self.age,self.rating)


