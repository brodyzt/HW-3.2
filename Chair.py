from Person import Person

class Chair:
    def __init__(self, id, person):
        self.id = id
        self.person = person

    def __str__(self):
        return 'Chair ID:{}, Person {}'.format(self.id, self.person)


class ChairStructure:
    counter = 0

    def __init__(self):
        self.structure = []

    def add_person(self, person):
        new_chair = Chair(self.counter, person)
        self.structure.append(new_chair)
        self.counter += 1

    def get_chair_at_index(self, index):
        return self.structure[index]

    def get_chair_with_id(self, id):
        for chair in self.structure:
            if chair.id == id:
                return chair
        else: return None

    def points_to(self, chair):
        try:
            return self.structure[self.structure.index(chair) + 1]
        except IndexError:
            return self.structure[0]

    def __str__(self):
        temp_str = ''
        for seat in self.structure:
            temp_str = temp_str + "Chair ID:{}, Person {}".format(seat.id, seat.person)
        return temp_str

    def remove_chair(self, input_id):
        for x in range(len(self.structure)):
            if input_id == self.structure[x].id:
                self.structure.pop(x)
                break
