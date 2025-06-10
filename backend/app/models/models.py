from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime

class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True)
    
    # Optional fields
    college = StringField()
    roll_number = StringField()
    department = StringField()
    subjects = StringField()
    child_name = StringField()
    relation = StringField()

    last_logged_in = DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'users'}
