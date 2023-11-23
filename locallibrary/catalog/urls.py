from django.urls import path, re_path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
