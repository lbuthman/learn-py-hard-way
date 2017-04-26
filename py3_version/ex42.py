# Animal is-a object
class Animal(object):
    pass


# Dog is-an Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-an Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-an Object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-an Animal
        self.animal = None


# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee inherits-a name
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


