from django.urls import path
from rec import views

urlpatterns = [
    path('rec/', views.rec_list),
    path('rec/shorts/<int:pk>/', views.rec_list_shorts),
    path('rec/<int:pk>/', views.rec_detail),
]
