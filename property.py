class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('Getting name')
        return self._name

    def setName(self, value):
        print('Setting name to ' + value)
        self._name = value

    def delName(self):
        print('Deleting name')
        del self._name

    # Set property to use getName, setName
    # and delName methods
    name = property(getName, setName, delName, 'Name property')


p = Person('Adam')
print(p.name)

p.name = 'John'

del p.name
