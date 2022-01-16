from model.person import Person

person1 = Person("tom",  33, ["python", "java"])

print(person1)

personList = []
personList = [Person("jane", 40, ["c#", "ruby"]), Person("nerma", 40, ["c#", "php"])]
print(personList[0].name)
print(personList[1].name)
personList.append(Person("bob", 40, ["java", "php", "pyton"]))
print(personList[2].name)