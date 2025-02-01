from ckeditor.fields import RichTextField
from django.db import models
from googletrans import Translator


def translate_text(text, dest_lang):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            translations_qs = FAQTranslation.objects.filter(faq=self)
            existing_languages = set(
                translations_qs.values_list('language', flat=True))
            new_translations = []
            for lang_code, lang_name in FAQTranslation.LANGUAGE_CHOICES:
                if lang_code not in existing_languages:
                    try:
                        translated_question = translate_text(
                            self.question, lang_code)
                        translated_answer = translate_text(
                            self.answer, lang_code)
                    except Exception as e:
                        print(f"Error while translating: {e}")
                        continue
                    new_translations.append(FAQTranslation(
                        faq=self,
                        language=lang_code,
                        question=translated_question,
                        answer=translated_answer
                    ))
            if new_translations:
                FAQTranslation.objects.bulk_create(new_translations)

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
