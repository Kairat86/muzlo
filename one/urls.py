from django.urls import path

from one import views

app_name = 'one'
urlpatterns = [
    path('', views.index, name='index'),
]
