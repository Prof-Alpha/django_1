from django.db import models

#------------------------------------------------------------------
PPriority = [
    ('L','Low'),
    ('M','Medium'),
    ('H', 'High'),
]

class classOne(models.Model):
    title                   = models.CharField(max_length=50)
    question                = models.TextField(max_length=400)
    priority                = models.CharField(max_length=50,choices=PPriority)

   # class Meta:
    #    verbose_name = "Questionn"
     #   verbose_name_plural = "Questionnss"
    def __str__(self):
        return self.title
#---------------------------------------------------------------------
class Questions(models.Model):
    name                    = models.CharField(max_length=30)
    describe                = models.TextField(max_length=200)

    def __str__(self):
        return self.name
# --------------------------------------------------------------------------
class vocab(models.Model):
    vocab                = models.CharField(max_length=200)
    function_1           = models.TextField(max_length=7000)
    function_2           = models.TextField(max_length=7000)
    status               = models.IntegerField()
    class_name           = models.CharField(max_length=50)

    def __str__(self):
        return self.vocab
#-----------------------------------------------------------------------------
class to_do(models.Model):
    task                    = models.CharField(max_length=200)

    def __str__(self):
        return self.task
    