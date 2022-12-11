from django.urls import path

from . import views
# from views import *


urlpatterns = [
    path('index/', views.index, name='index'),
    path('max/',views.max , name='max'),
    path('hello/',views.person_list ,name='hello'),
    path('man/',views.peak , name='man'),
    path('add',views.add , name='add'),
    path('',views.sub , name='sub')
]
