from lib.db import db
from mongoengine import *
from  .persistable import Persistable


class Users(db.Document):
    name = StringField()
    age = IntField()
        




baseModel = Persistable(Users)

def createUser(**kwargs):
    return baseModel.create(**kwargs)

def fetch(page=1, per_page=10, **query):
    return baseModel.fetch(page, per_page, **query)