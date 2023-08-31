
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name="glav"),
    path('<slug:slug>/', views.MovieAbout.as_view(), name="movie_about"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
]
