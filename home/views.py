from django.core.cache import cache
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FAQ, FAQTranslation
from .serializers import FAQSerializer


class FAQView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f"faqs_{lang}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(data={
                "success": "true",
                "data": cached_data
            }, status=status.HTTP_200_OK)

        faqs = FAQ.objects.prefetch_related(
            Prefetch(
                "translations",
                queryset=FAQTranslation.objects.filter(language=lang),
                to_attr="filtered_translations"
            )
        ).all()

        serializer = FAQSerializer(faqs, many=True)
        cache.set(cache_key, serializer.data, timeout=3600)
        return Response(data={
            "success": "true",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
