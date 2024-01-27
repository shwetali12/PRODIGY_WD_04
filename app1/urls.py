from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('resume/',views.resume,name='resume'),
    path('work/',views.work,name='work'),
    path('contact/',views.contact,name='contact'),
    path('success/', views.success, name='success'),

   
]
