from django.contrib import admin

from .models import FAQ, FAQTranslation


class FAQTranslationInline(admin.StackedInline):
    model = FAQTranslation
    extra = 0


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    inlines = [FAQTranslationInline]


admin.site.register(FAQ, FAQAdmin)
