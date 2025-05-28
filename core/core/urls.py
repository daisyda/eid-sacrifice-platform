from django.urls import path
from . import views

urlpatterns = [
    path('', views.donor_search, name='donor_search'),
    path('status/', views.donor_status, name='donor_status'),
]
