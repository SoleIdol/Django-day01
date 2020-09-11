from django.conf.urls import url

from One import views

urlpatterns = [
    url(r'^one1/', views.one1),
    url(r'^one2/', views.one2),
    
]
