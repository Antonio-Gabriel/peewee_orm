from src.models.Models import Group

class GroupRepository:
    def create(self, name: str, owner: int):
        result = Group.create(
            name = name,
            owner = owner
        )

        return result