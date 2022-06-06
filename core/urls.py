from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.IndexSite.as_view(), name="inicio"),
    path('get_ramos', views.get_ramos, name="get_ramos"),
    path('ramo_best_match_from_text', views.ramo_best_match_from_text, name="ramo_best_match_from_text"),
    path('ramo/<int:ramo_id>', views.Ramo.as_view(), name="ramo"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)