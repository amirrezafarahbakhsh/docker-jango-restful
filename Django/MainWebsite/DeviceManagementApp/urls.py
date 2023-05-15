from django.urls import path
from . import views


urlpatterns = [
    path('', views.testViewFromApp_view),
    path('addDevice/', views.AddDeviceView.as_view()),
    path('listDevice/', views.ListDevicesView.as_view()),
]
