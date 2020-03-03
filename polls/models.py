from django.db import models

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200) #}
    question_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
