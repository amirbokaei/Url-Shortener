from django.urls import path

from . import views

app_name = 'urlshorter'

urlpatterns = [
    path('', views.shortetView.as_view(), name='index'),
    path('s/<str:uuid>/' ,views.redirectView.as_view() , name = "redirect")

]
