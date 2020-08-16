from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('pdfs/', views.pdfs, name="pdfs"),
    path('chat/', views.chat, name="chat"),
    path('room/<str:room_name>/', views.room, name="room")
]
