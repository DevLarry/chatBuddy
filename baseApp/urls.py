from django.urls import path
from . import views


urlpatterns =[
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('room/<int:idParam>/', views.room, name="room"),
    
    path('create_room', views.createRoom, name="createRoom" ),
    path('update_room/<int:id>', views.updateRoom, name="updateRoom" ),
    path('delete_room/<int:id>', views.deleteRoom, name="deleteRoom" ),
]