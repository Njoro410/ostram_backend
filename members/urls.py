from django.urls import path
from .views import *

urlpatterns = [
    path('members/', members_list, name='members'),
    path('member/<int:member_no>/', member_detail, name='member_detail'),
    path('residential_areas/', residential_list, name='residential_areas'),
    path('residential_area/<int:residential_id>/',
         residential_area_detail, name='residential_area_detail'),
]
