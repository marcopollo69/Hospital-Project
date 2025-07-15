from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete ),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('delete/<int:id>', views.delete ),
    path('edit/<int:id>', views.edit, name='edit'),

    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.departments, name='departments'),

    #mpesa URLs

    path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
