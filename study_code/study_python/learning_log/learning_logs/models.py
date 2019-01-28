from django.db import models

# Create your models here.
class Topic(models.Model):
    """learning_log"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the string of models"""
        return self.text

class Entry(models.Model):
    """specific knowledge of some topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """retrun the string of models"""
        return self.text[:50] + "..."
