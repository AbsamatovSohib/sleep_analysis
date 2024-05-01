from django.urls import path
from intro import views

urlpatterns = [
    path("list/", views.IntroListView.as_view()),
    path("notification/", views.NotificationListView.as_view()),
]
