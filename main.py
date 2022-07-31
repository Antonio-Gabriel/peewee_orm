from src.repository.GroupRepository import GroupRepository
from src.repository.PersonRepository import PersonRepository

group_repository = GroupRepository()
# group_repository.create("Mixtaker", 1)

person_repository = PersonRepository()
# person_repository.create('António Gabriel', 'antoniogabriel@gmail.com', '@antoniocampos20')
person_with_group = person_repository.get_person_with_group()
print(person_with_group.name)
# person = person_repository.find_by_email("antoniogabriel@gmail.com")
# print(person.name)

