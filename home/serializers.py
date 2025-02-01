from rest_framework import serializers

from .models import FAQ, FAQTranslation


class FAQTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQTranslation
        fields = ['language', 'question', 'answer']


class FAQSerializer(serializers.ModelSerializer):
    question = serializers.CharField()
    answer = serializers.CharField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        translations = instance.filtered_translations
        if translations:
            translated = translations[0]
            return {
                "id": instance.id,
                "question": translated.question,
                "answer": translated.answer,
            }

        return {
            "id": instance.id,
            "question": instance.question,
            "answer": instance.answer,
        }
