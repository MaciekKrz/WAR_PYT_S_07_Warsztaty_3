from django.db import models
from django.contrib.auth.models import Permission, User


class Room(models.Model):
    name = models.CharField(max_length=64)
    seats = models.IntegerField(null=True)
    projector = models.BooleanField()

    class Meta:
        permissions = (
            ("add_group", "Can add group"),
        )

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateTimeField('%m-%d-%Y')
    comment = models.TextField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%m-%d-%Y")

#########################################################
class Lecture(models.Model):
    name = models.CharField(max_length=64)
    lecturer = models.CharField(max_length=64)


class Student(models.Model):
    name = models.CharField(max_length=64)
    year_at_university = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    lecture = models.ManyToManyField(Lecture, through='Week')


class Week(models.Model):
    day = models.CharField(max_length=124)
    students = models.ForeignKey(Student, related_name="students", on_delete=models.CASCADE)
    lectures = models.ForeignKey(Lecture, related_name="lectures", on_delete=models.CASCADE)

