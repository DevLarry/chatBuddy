from django.urls import path

from . import views


urlpatterns =[
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('room/<int:idParam>/', views.room, name="room"),
    path('profile/<int:id>', views.userProfile, name="profile"),
    path('create_room', views.createRoom, name="createRoom" ),
    path('update_room/<int:id>', views.updateRoom, name="updateRoom" ),
    path('delete_room/<int:id>', views.deleteRoom, name="deleteRoom" ),
    path('deleteMsg/<int:id>', views.deleteMsg, name="deleteMsg" ),

    path('editMsg/<int:id>', views.editMsg, name="editMsg" ),

    path('edit_user', views.editUser, name='edit_user'),
]