from mongoengine import *
class PushHobby(Document):
    name=StringField()
    info=StringField()
    pics=StringField()
    link=StringField()