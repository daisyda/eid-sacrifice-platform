from django.urls import path
from . import views  # ✅ Make sure this line exists and views.py is present

urlpatterns = [
    path('', views.donor_search, name='donor_search'),
    path('status/', views.donor_status, name='donor_status'),
    path('adminpanel/', views.admin_panel, name='admin_panel'),  
]
