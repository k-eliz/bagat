from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("about_company", views.info, name="info"),
    path("our_advantages", views.advantages, name="advantages"),
]