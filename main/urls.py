from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path('', movie_list),
    path('detail/<int:pk>/', movie_detail),

]