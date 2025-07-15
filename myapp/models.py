from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    medical_history = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname

class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    Doctorid = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


#CREATE A WARD MODEL ---- name, capacity, department, floor

class Ward(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    department = models.CharField(max_length=100)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone =  models.CharField(max_length=20)
    date_time = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"