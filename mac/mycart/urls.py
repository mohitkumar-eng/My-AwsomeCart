from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"), 
    path('about',views.about,name="index"),
    path('contact',views.contact,name="index"), 
    path('search',views.search,name="index"),
    path('tracker',views.tracker,name="index"),
    path('products/<int:myid>',views.productview,name="index"),
    path('checkouts',views.checkouts,name="index"),
    
]