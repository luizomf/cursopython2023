from blog import views
from django.urls import path

# blog/
urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]
