from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rec import views

urlpatterns = [
    path('apart/', views.ApartmentsList.as_view()),
    path('apart/<int:pk>/', views.ApartmentstDetail.as_view()),
    path('apart/search/', views.SearchApartmentsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

