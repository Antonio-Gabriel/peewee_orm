from datetime import datetime

from src.models.BaseModel import BaseModel, sqlite_db
from peewee import TextField, ForeignKeyField, DateTimeField

class Person(BaseModel):
    name: str = TextField()
    email: str = TextField(unique=True)
    password: str = TextField()


class Group(BaseModel):
    name = TextField()
    owner = ForeignKeyField(Person, backref='groups')

class Note(BaseModel):
    owner = ForeignKeyField(Person, backref='notes')
    group = ForeignKeyField(Group, backref='notes', null=True, default=None)
    title = TextField()
    note = TextField()
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField()

# Person.create_table()
sqlite_db.create_tables([Person, Group, Note])