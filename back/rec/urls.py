from django.urls import path
from rec import views

urlpatterns = [
    path('apartments_list/', views.apartments_list),
]
