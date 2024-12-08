from mongoengine import Document, StringField, ListField, connect

# Connect to MongoDB
connect(db="rbac_api", host="localhost", port=27017)

# User model
class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True, choices=["admin", "user"])

# Project model
class Project(Document):
    name = StringField(required=True)
    description = StringField()
    created_by = StringField(required=True)
