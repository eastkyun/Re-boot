from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rec import views

urlpatterns = [
    path('apart/', views.apartments_list),
    path('apart/<int:pk>/', views.apartments_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

