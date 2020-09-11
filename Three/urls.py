from django.conf.urls import url

from Three import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^test/', views.test),
]
