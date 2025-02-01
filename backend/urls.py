from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),
]


admin.site.site_header = "BharatFD"
admin.site.site_title = "BharatFD"
admin.site.index_title = "BharatFD"
