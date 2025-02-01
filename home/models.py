from ckeditor.fields import RichTextField
from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'faqs'


class FAQTranslation(models.Model):
    LANGUAGE_CHOICES = [
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE,
                            related_name="translations")
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    question = models.TextField()
    answer = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.faq.question} ({self.language})"

    class Meta:
        db_table = 'faq_translations'
        unique_together = ('faq', 'language')
