from django.urls import path
from . import views
app_name='bank'

urlpatterns=[
    path('',views.home,name='home'),
    path('', views.img, name='img'),

    path('',views.About, name='About'),
    path('login/', views.login, name='login'),
    path('Register/', views.Register, name='Register'),
    path('new_page/', views.new_page, name='new_page'),
    path('new/', views.new, name='new')

]
