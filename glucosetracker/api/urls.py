from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/levels/reading/<int:reading_id>/",
        views.glucose_reading,
        name="glucose_reading",
    ),
    path("v1/levels/user/<str:user_id>/", views.user, name="user"),
]
