from django.urls import path

from delano_bar.core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]