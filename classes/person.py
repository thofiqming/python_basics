class Person:
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def get_details(self):
        return 'name= {}, age= {}, gender={}, salary={}'.format(self.name, self.age, self.gender, self.salary)

    # just like a constructor
    @classmethod
    def create_person(cls, values):
        name, age, gender, salary = values.split(":")
        return cls(name, age, gender, salary)

    @staticmethod
    def get_retirement_age(age):
        if age >= 20:
            return age + 10
        elif age > 60:
            return age
        else:
            return "still you are too young"


person = Person('thofiq', '32', 'male', 20000)
print(person.get_details())

person1 = Person.create_person('thofiq:32:male:20000')
print(person1.get_details())

print(Person.get_retirement_age(40))
