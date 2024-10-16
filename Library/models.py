from django.db import models

# Create your models here.
class Book(models.Model):
    book_id=models.CharField(max_length=12,primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    published_year=models.IntegerField(max_length=12)
class Student(models.Model):
    student_id=models.CharField(max_length=12,primary_key=True)
    student_name=models.CharField(max_length=100)
    student_phone=models.CharField(max_length=15)
    student_email=models.EmailField(max_length=50)
    stud_status=models.CharField(max_length=15, default='Active')
class Borrowing(models.Model):
    borrow_id=models.CharField(max_length=12,primary_key=True)
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    borrow_date=models.DateField(max_length=15)
    return_date=models.DateField(max_length=15)
class Course(models.Model):
    code=models.CharField(max_length=4,primary_key=True)
    description=models.TextField()
class Mentor(models.Model):
    menid=models.CharField(max_length=8,primary_key=True)
    menname=models.TextField(max_length=225)
    menroomno=models.CharField(max_length=3,default='sk2')



