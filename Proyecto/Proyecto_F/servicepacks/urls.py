from . import views
from django.urls import path

urlpatterns = [      
    path('', views.servicepacks, name='servicepacks'),
    path('servicepack_status_/<int:servicepack_id>/', views.change_status_servicepack, name='servicepack_status'),
    path('create/', views.create_servicepack, name='create_servicepack'),     
]