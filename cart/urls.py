from django.urls import path
from cart import views

urlpatterns = [
    path("list/", views.CartItemsListView.as_view()),
]
