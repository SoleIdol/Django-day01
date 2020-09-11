from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^food/', views.foods),
    url(r'^hello/', views.hello),
]
