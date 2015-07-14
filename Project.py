from Sort import Sort
from Person import Person
from Chair import ChairStructure

structure = ChairStructure()

file = open('People','r')
contents = file.readlines()
contents.pop(0)
for line in contents:
    structure.add_person(Person(line.split(',')))
    Person.counter += 1

running = True

while running:
    print('What would you like to do? Select the number of the corresponding option.')
    print('1.Add Person:\n2.Remove Person\n3.Determine who a chair points to\n')
    choice = input('Choice: ')

    print('\n' * 10)

    if choice == '1':
        name = input('The name of the person: ')
        age = input('The age of the person: ')
        rating = input('The personality rating of the  person: ')
        structure.add_person(Person([name, age, rating]))

    if choice == '2':
        print('The following data is the list of all people sitting in the seat structure.\n')
        print(str(structure) + '\n')
        print('Enter the Chair ID of the person you want to remove: ')
        chair_id = input('ID: ')
        while True:
            try:
                chair_id = int(chair_id)
                break
            except ValueError:
                print("You didn't enter a valid ID. Please try again.")
                chair_id = input('ID: ')

        structure.remove_chair(chair_id)

    if choice == '3':
        print('The following data is the list of all people sitting in the seat structure.\n')
        print(str(structure) + '\n')
        print('Enter a chair ID to determine who that chair points to: ')
        chair_id = input('ID: ')
        while True:
            try:
                chair_id = int(chair_id)
                break
            except ValueError:
                print("You didn't enter a valid ID. Please try again.")
                chair_id = input('ID: ')

        print('The chair points to {}\n\n'.format(structure.points_to(structure.get_chair_with_id(chair_id)).person))
