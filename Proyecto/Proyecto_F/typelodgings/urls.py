from . import views
from django.urls import path

urlpatterns = [      
    path('', views.typelodgings, name='typelodgings'),
    path('typelodging_status_/<int:typelodging_id>/', views.change_status_typelodging, name='typelodging_status'),           
]