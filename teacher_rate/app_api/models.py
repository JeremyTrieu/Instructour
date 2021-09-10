from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length = 200, null=False)
    school_address = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.school_name

class Subject(models.Model):
    subject_name = models.CharField(max_length = 100, null=False)
    subject_code = models.CharField(max_length = 100, default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

class Professor(models.Model):
    name = models.CharField(max_length = 100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    detail = models.CharField(max_length = 400, null=False)
    professor_rate = models.DecimalField(max_digits = 5, decimal_places=2, null=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.detail