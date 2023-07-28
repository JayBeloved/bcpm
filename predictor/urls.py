from django.urls import path, include
from . import views

urlpatterns = [
    path('', include(([
        path('', views.landing, name='landing'),
        path('model/landing', views.index, name="index"),
    ], 'bcpm'), namespace='model')),
]


