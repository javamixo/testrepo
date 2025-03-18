from django.contrib import admin
from django.urls import path, include
from cakes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cakes/', views.cake_list, name='cake_list'),
    path('order/', views.order_cake, name='order_cake'),
    path('', include('cakes.urls')), #add this line
]