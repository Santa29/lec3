from django.urls import path
from .views import homePageView, aboutPageView, infoPageView

urlpatterns = [
    path('', homePageView.as_view(), name = 'home'),
    path('about/', aboutPageView.as_view(), name = 'about'),
    path('info/', infoPageView.as_view(), name  = 'info')
]