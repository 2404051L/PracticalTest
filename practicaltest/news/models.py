from django.db import models

class Story(models.Model):
    story_title = models.CharField(max_length=50)
    published_date = models.DateTimeField('date published')
    story_text = models.CharField(max_length=200)

    def __str__(self):
        return self.story_text
