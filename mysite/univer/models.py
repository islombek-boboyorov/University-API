from django.db import models


class University(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    university = models.ForeignKey(University, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Chair(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Group(models.Model):
    number = models.CharField(max_length=128, blank=False, null=False)
    teacher_name = models.CharField(max_length=128, blank=False, null=False)
    pupil_count = models.PositiveIntegerField(blank=False, null=False, default=0)
    chair = models.ForeignKey(Chair, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.teacher_name


class Teacher(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    subject = models.CharField(max_length=128, blank=False, null=False)
    university = models.ForeignKey(University, blank=False, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    chair = models.ForeignKey(Chair, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    chair = models.ForeignKey(Chair, blank=False, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
