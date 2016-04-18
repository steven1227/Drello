from app import db
from flask import url_for
import datetime


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return '<Post %r>' % (self.body)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class User(db.DynamicDocument):
    account_type = db.StringField(max_length=255, required=True)
    email = db.EmailField(required=True,unique=True)
    password = db.StringField(max_length=255, required=True)
    name = db.StringField(max_length=255, required=True)
    image = db.ImageField(size=(500,500,True))
    address = db.StringField(max_length=255, required=True)
    phone = db.StringField(max_length=255,unique=True)

#Can be intergate into User
#Todo
class Patient(db.Document):
    user_id = db.ReferenceField(db.ObjectId,required=True)
    sex = db.StringField(max_length=255, required=True)
    birthdate = db.DateTimeField(required=True);
    name = db.StringField(max_length=255, required=True)
    blood = db.ReferenceField(db.ObjectId)


class Admin(db.Document):
    user_id = db.ReferenceField(db.ObjectId)

class Department(db.Document):
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)

class Appointment(db.Document):
     date = db.DateTimeField(required=True);
     patient = db.EmbeddedDocumentField('Patient')

class Precription(db.Document):
     date = db.DateTimeField(required=True);
     patient = db.EmbeddedDocumentField('Patient')

class Bed(db.Document):
    bed_number = db.IntField(required=True)
    bed_type = db.StringField(max_length=255, required=True)
    patient = db.EmbeddedDocumentField('Patient',required=True)
    allotment_date = db.DateTimeField(required=True)
    discharge_date = db.DateTimeField(required=True)

class BloodBankDonner(db.Document):
    name = db.StringField(max_length=255, required=True)
    sex = db.StringField(max_length=255, required=True)
    blood = db.ReferenceField(db.ObjectId)
    last_donation_date = db.DateTimeField(required=True)

class BloodBankStatus(db.Document):
    blood_group = db.StringField(max_length=255, required=True,unique=True)
    status = db.IntField(required=True)

class Report(db.Document):
    type = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    date = db.DateTimeField(required=True)
    patient = db.EmbeddedDocumentField('Patient')

class Message(db.Document):
    from_who = db.EmbeddedDocumentField('User')
    content = db.StringField(max_length=255, required=True)

class Event(db.Document):
    date = db.DateTimeField(required=True)
    content = db.StringField(max_length=255, required=True)

#Can be intergate into User
class Doctor(db.Document):
    user_id = db.ReferenceField(db.ObjectId,require=True)
    department = db.EmbeddedDocumentField('Department')
    appointments = db.ListField(db.EmbeddedDocumentField('Appointment'))
    precriptions = db.ListField(db.EmbeddedDocumentField('Precription'))
    patients = db.ListField(db.EmbeddedDocumentField('Patient'))
    reports = db.ListField(db.EmbeddedDocumentField('Report'))
    messages = db.ListField(db.EmbeddedDocumentField('Message'))

class Invoice(db.Document):
    invoice_number = db.IntField(required=True)
    title =  db.StringField(max_length=255, required=True)
    patient = db.EmbeddedDocumentField('Patient')
    creation_date = db.DateTimeField(required=True)
    due_date = db.DateTimeField(required=True)
    vat_per = db.IntField(required=True)
    discount_amount = db.IntField(required=True)
    status = db.StringField(max_length=255, required=True)

#Can be intergate into User
class accountant(db.Document):
    user_id = db.ReferenceField(db.ObjectId,require=True)
    invoice = db.ListField(db.EmbeddedDocumentField('Invoice'))

#Can be intergate into User
class Nurse(db.Document):
    user_id = db.ReferenceField(db.ObjectId,require=True)
    patients = db.ListField(db.EmbeddedDocumentField('Patient'))
    reports = db.ListField(db.EmbeddedDocumentField('Report'))

#Todo Pharmacist and Receptionist