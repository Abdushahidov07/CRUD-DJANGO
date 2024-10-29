from django.urls import path, include
from .views import *

urlpatterns = [
    path('', menu, name="menu"),
    path('showcompany/', show_all_company, name="allcompany"),
    path('createcomp/', create_company, name="createcomp"),
    path('updatecomp/<int:pk>', update_company, name="updatecomp"),
    path('deletecopm/<int:pk>', delete_company, name="deletecomp"),
    path('showcar/', show_all_car, name="allcar"),
    path('createcar/', create_car, name="createcar"),
    path('updatecar/<int:pk>', update_car, name="updatecar"),
    path('deletecar/<int:pk>', delete_car, name="deletecar"),
    path('getcompid/<int:pk>', getcomp_by_id, name="getcompid"),
    path('getcarid/<int:pk>', getcar_by_id, name="getcarid"),
]
