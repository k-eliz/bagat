from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("about-company", views.info, name="info"),
    path("our-advantages", views.advantages, name="advantages"),
    path("priority-directions", views.priority_directions, name="priority-directions"),
]