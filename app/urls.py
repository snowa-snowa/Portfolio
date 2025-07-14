from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1.as_view(), name='page1'),
    path('page2/', views.page2.as_view(), name='page2'),
]