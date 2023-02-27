from django.db import models

class Question(models.Model):
    answer_methodType = models.TextChoices('Answer Method', 'None Radio-Button Check-Box')
    name = models.TextField()
    answer_method = models.CharField(max_length=50, choices=answer_methodType.choices)
    other_method = models.BooleanField()
    other_title = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=500)
    
    date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.question.name)


class UsersInfo(models.Model):
    email = models.EmailField(max_length=500)
    issues = models.TextField(null=True)
    more_issue = models.TextField(null=True)
    full_information_issue = models.TextField(null=True)
    phrase = models.TextField()
    
    date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Users Info'
    
    def __str__(self):
        return str(self.email)