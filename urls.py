from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='About Us'),
    path('policy/', views.policy, name='policy'),

    path('<slug:slug>/', views.post_detail, name='post_detail'),

]