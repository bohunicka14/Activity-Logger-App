from mongoengine import *


class Activity(Document):
    id = IntField(primary_key=True)
    name = StringField(required=True)
    duration = IntField()

class Timestamps(Document):
    id = IntField(primary_key=True)
    activity = ReferenceField(Activity)
    _from = DateTimeField()
    _to = DateTimeField()
