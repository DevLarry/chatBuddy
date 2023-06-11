from django.test import SimpleTestCase
from django.urls import reverse, resolve
from baseApp.views import (activity, createRoom, deleteMsg, deleteRoom, editMsg, editUser, home,
    loginUser, logoutUser, registerUser, room, topics, updateRoom, userProfile)


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        home_url = reverse("home")
        self.assertEquals(resolve(home_url).func, home)

    def test_login_url_resolves(self):
        login_url = reverse("login")
        self.assertEquals(resolve(login_url).func, loginUser)

    def test_register_url_resolves(self):
        register_url = reverse("register")
        self.assertEquals(resolve(register_url).func, registerUser)

    def test_logout_url_resolves(self):
        logout_url = reverse("logout")
        self.assertEquals(resolve(logout_url).func, logoutUser)

    def test_create_room_url_resolves(self):
        create_room_url = reverse("createRoom")
        self.assertEquals(resolve(create_room_url).func, createRoom)

    def test_edit_user_url_resolves(self):
        edit_user_url = reverse("edit_user")
        self.assertEquals(resolve(edit_user_url).func, editUser)

    def test_activity_url_resolves(self):
        activity_url = reverse('activity')
        self.assertEquals(resolve(activity_url).func, activity)
        
    def test_topics_url_resolves(self):
        topics_url = reverse('topics')
        self.assertEquals(resolve(topics_url).func, topics)

    def test_room_url_resolves(self):
        room_url = reverse("room", args=[1])
        self.assertEquals(resolve(room_url).func, room)

    def test_profile_url_resolves(self):
        profile_url = reverse("profile", args=[1])
        self.assertEquals(resolve(profile_url).func, userProfile)

    def test_update_room_url_resolves(self):
        updateRoom_url = reverse("updateRoom", args=[1])
        self.assertEquals(resolve(updateRoom_url).func, updateRoom)

    def test_delete_room_url_resolves(self):
        deleteRoom_url = reverse("deleteRoom", args=[1])
        self.assertEquals(resolve(deleteRoom_url).func, deleteRoom)

    def test_delete_Msg_url_resolves(self):
        deleteMsg_url = reverse("deleteMsg", args=[1])
        self.assertEquals(resolve(deleteMsg_url).func, deleteMsg)

    def test_edit_Msg_url_resolves(self):
        editMsg_url = reverse("editMsg", args=[1])
        self.assertEquals(resolve(editMsg_url).func, editMsg)
