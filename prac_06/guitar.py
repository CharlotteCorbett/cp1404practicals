"""Guitar class that creates Guitar objects"""

class Guitar:
    def __init__(self, name='', year=0, cost=0.0, age=0):
        self.age = age
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        CURRENT_YEAR = 2022
        self.age = CURRENT_YEAR - self.year
        return self.age

    def is_vintage(self):
        VINTAGE_AGE = 50
        self.get_age()
        if self.age >= VINTAGE_AGE:
            return True
        else:
            return False