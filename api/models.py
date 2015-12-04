from django.db import models
from enum import Enum


# Create your models here.

class SectionTypes(Enum):
    Foreword = 'F'
    Preface = 'P'
    Chapter = 'C'
    References = 'R'


class Chapter(models.Model):
    Book = models.ForeignKey('Book', on_delete=models.CASCADE)
    Number = models.IntegerField()
    Title = models.CharField(max_length=128)
    SectionType = SectionTypes.Chapter


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    PublicUrl = models.CharField(max_length=1024)
    Author = models.CharField(max_length=255)
    PageCount = models.IntegerField()
    Chapters = models.ManyToOneRel(Chapter, to="Chapter", field_name="Book")
