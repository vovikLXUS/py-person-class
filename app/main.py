class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    persons = []
    for person in people_list:
        name = person["name"]
        age = person["age"]
        person = Person(name, age)
        persons.append(person)

    for people, person in zip(people_list, persons):
        wife_name = people.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = people.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return persons
