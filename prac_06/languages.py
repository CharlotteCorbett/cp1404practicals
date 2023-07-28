"""ProgrammingLanguage Class Task"""

class ProgrammingLanguage:
    """Create a Programming Language object"""
    def __init__(self, name='', typing='', reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            self.reflection = True
        else:
            self.typing = False