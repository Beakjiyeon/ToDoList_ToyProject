from django.contrib import admin
from django.urls import path,include
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',board.views.index,name='index'),
   
]
