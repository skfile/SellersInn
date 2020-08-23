from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('register', views.register, name="signup"),
    path('sample1', views.sample1, name="samplereport1"),
    path('sample2', views.sample2, name="samplereport2"),
    path('sample3', views.sample3, name="samplereport3"),
]
