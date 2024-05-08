'''
An object-relational mapper (ORM) is a programming technique often used in web development to convert data between
incompatible type systems in object-oriented programming languages and relational databases.
It essentially acts as a translator between the object-oriented world of application  code and the relational world of
database management systems. By using an ORM, developers can interact with databases using objects
and classes rather than writing complex SQL queries, making database interactions more intuitive and efficient.
Some popular ORM frameworks include Hibernate for Java,  Entity Framework for .NET, and SQLAlchemy for Python.
Peewee
'''


from peewee import *

db = MySQLDatabase('graviola_05', user='root', password='P@ssw0rd', host='localhost', port=3306)

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


db.connect()
db.create_tables([Person, Pet])

