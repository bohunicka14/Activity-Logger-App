from mongoengine import *


class Activity(Document):
    #_id = ObjectIdField(primary_key=True)
    name = StringField(required=True)
    duration = IntField()

class Timestamps(Document):
    #_id = ObjectIdField(primary_key=True)
    activity = ReferenceField(Activity)
    _from = DateTimeField()
    _to = DateTimeField()
