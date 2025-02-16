from django.db import models
from django.urls import reverse

from django.core.validators import MinValueValidator, MaxValueValidator

class field(models.Model):
    
    FIELD_CHOICES = [
    (1, "教養教育科目 人文分野"),
    (2, "教養教育科目 社会分野"),
    (3, "教養教育科目 自然分野"),
    (4, "教養教育科目 ライフデザイン分野"),
    
    ]
    
    field = models.IntegerField(
        null=True, 
        blank=True,
        choices=FIELD_CHOICES
        )

    def __str__(self):
        field_dict = dict(self.FIELD_CHOICES)
        return field_dict.get (self.field, "None")

class semester(models.Model):
    
    SEMESTER_CHOICES  = [
        (1,"前期"),
        (2,"後期"),
        (3,"通年"),
    ]
    
    semester = models.IntegerField(
        default = 0,
        choices = SEMESTER_CHOICES
    )

    def __str__(self):
        semester_dict= dict(self.SEMESTER_CHOICES)
        return semester_dict.get (self.semester, "None")

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
        choices=DAY_OF_WEEK_CHOICES
    )

    def __str__(self):
        day_of_week_dict= dict(self.DAY_OF_WEEK_CHOICES)
        return day_of_week_dict.get (self.day_of_week, "None")
    
class period(models.Model):
    PERIOD_CHOICES = [
        (1,"1時限"),
        (2,"2時限"),
        (3,"3時限"),
        (4,"4時限"),
        (5,"5時限"),
        (6,"6時限"),
        (7,"7時限"),
    ]

    period = models.IntegerField(
        default=0,
        choices = PERIOD_CHOICES
        )
    
    def __str__(self):
        period_dict= dict(self.PERIOD_CHOICES)
        return period_dict.get (self.period, "None")
    
class code(models.Model):
        code = models.IntegerField(
        default=0,
        )

        def __str__(self):
            return str(self.code) if self.code != 0 else "None"


class Class(models.Model):
    name = models.CharField(
        max_length=100,
        null = True,
        blank=True
        )

    teacher = models.CharField(
        max_length = 50,
        null  = True,
        blank=True
        )

    field = models.ManyToManyField(field, blank = True)
    semester = models.ManyToManyField(semester, blank=True)
    day_of_week = models.ManyToManyField(day_of_week, blank=True)
    period = models.ManyToManyField(period, blank=True)
    code = models.ManyToManyField(code, blank=True)


    def __str__(self):
        return self.name 
    
    
    def get_absolute_url(self):
        return reverse('forms:class_detail', kwargs={'id':self.id})
    
    def get_absolute_group_url(self, group_id=None):
        if group_id:
            return reverse('forms:group_classform', kwargs={'id':self.id, 'group_id':group_id})
        return reverse('forms:class_detail', kwargs={'id':self.id})
        

class Group(models.Model):
    name = models.CharField(
        max_length = 50,
        null=True, 
        blank=True
        )
    
    def __str__(self):
        return self.name 
    

class Answer(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default = 1)

    group = models.ForeignKey(Group, on_delete=models.SET_DEFAULT, default= 1 )

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

