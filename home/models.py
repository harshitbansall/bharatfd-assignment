from ckeditor.fields import RichTextField
from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'faqs'
