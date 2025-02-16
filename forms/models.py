"""from django.db import models
from django.urls import reverse

from django.core.validators import MinValueValidator, MaxValueValidator

class TestModel(models.Model):
    question_text1 = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=200)

class Field(models.Model):
    
    field_choices = [
    (1, "教養教育科目 人文分野"),
    (2, "教養教育科目 社会分野"),
    (3, "教養教育科目 自然分野"),
    (4, "教養教育科目 ライフデザイン分野"),
    
    ]
    
    field = models.IntegerField(
        null=True, 
        blank=True,
        choices=field_choices
        )

    def __str__(self):
        return self.field

class semester(models.Model):
    
    SEMESTER_CHOICES  = [
        (1,"前期"),
        (2,"後期"),
        (3,"通年"),
    ]
    
    semester = models.IntegerField(
        default = 0,
        null = True,
        blank=True,
        choices = SEMESTER_CHOICES
    )

class day_of_week(models.Model):
    
    DAY_OF_WEEK_CHOICES = [
        (1, "月曜日"),
        (2, "火曜日"),
        (3, "水曜日"),
        (4, "木曜日"),
        (5, "金曜日"),
        (6, "土曜日"),
        (7, "特曜日"),
    ]

    day_of_week = models.IntegerField(
        default=0, 
        null=True, 
        blank=True, 
        choices=DAY_OF_WEEK_CHOICES
    )
    
class period(models.Model):
    PERIOD_CHOICES = [
        (1,"1時限"),
        (2,"2時限"),
        (3,"3時限"),
        (4,"4時限"),
        (5,"5時限"),
        (6,"6時限"),
        (7,"7時限"),
        (8,"特曜日"),
    ]

    period = models.IntegerField(
        default=0,
        null=True, 
        blank=True,
        choices = PERIOD_CHOICES
        )

class code(models.Model):
        code = models.IntegerField(
        default=0,
        null=True,
        blank=True
        )


class Class(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )

    teacher = models.CharField(
        max_length = 50,
        null=True,
        blank=True
        )

    fields = models.ManyToManyField(Field, blank = True)
    semester = models.ManyToManyField(semester, blank=True)
    days_of_week = models.ManyToManyField(day_of_week, blank=True)
    period = models.ManyToManyField(period, blank=True)
    codes = models.ManyToManyField(code, blank=True)


    def __str__(self):
        return self.name 
    
    
    

class Answer(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default = 1)

    vote = models.IntegerField(
        default = 0
    )
    
    credit = models.CharField(
        max_length= 50,
        default = "----"
   )

    score = models.CharField(
        max_length= 50,
        default = "----"
    )

    homework = models.CharField(
        max_length= 50,
        default = "----"
    )

    explanation = models.CharField(
        max_length= 50,
        default = "----"
    )

    passion = models.CharField(
        max_length= 50,
        default = "----"
    )

    recommend = models.CharField(
        max_length= 50,
        default = "----"
    )

    GoodComment = models.CharField(
        max_length= 400,
        default = "----"
    )

    BadComment = models.CharField(
        max_length= 400,
        default = "----"
    )

    OtherComment = models.CharField(
        max_length = 400,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.Class.name

class Group(models.Model):
    name = models.CharField(
        max_length = 50,
        null=True, 
        blank=True
        )
    
    code = models.IntegerField(
        default=0,
        null=True,
        blank=True
        )
    
    vote = models.IntegerField(
        default=0
        )
    
    def __str__(self):
        return self.name """