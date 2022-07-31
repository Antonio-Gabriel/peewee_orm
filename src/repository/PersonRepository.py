from src.models.Models import Person, Group

class PersonRepository:

    def create(self, name: str, email: str, password: str):
        person = Person(
            name=name,
            email=email,
            password=password
        )

        result = person.save()

        return result
    
    def find_by_email(self, email: str):
        """find person by email"""
        return Person.select().where(Person.email == email).get()
    
    def get_person_with_group(self):
        """get person with group"""
        return (
            Group.select()
            .join(Person)
            .get()
        )