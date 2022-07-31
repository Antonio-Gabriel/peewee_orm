from peewee import SqliteDatabase, Model

sqlite_db = SqliteDatabase("notes.db")

class BaseModel(Model):    
    class Meta:
        database = sqlite_db