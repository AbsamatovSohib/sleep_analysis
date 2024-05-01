from django.urls import path
from cart import views

urlpatterns = [
    path("total/", views.CartTotalPriceAPIView.as_view()),
    path("list/", views.CartItemView.as_view()),
]
