from prac_06.languages import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in languages:
    language.is_dynamic()
    if language.reflection is True:
        print(language.name)
