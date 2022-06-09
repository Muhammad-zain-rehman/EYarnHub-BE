from django.urls import path, include

from Api.Users.views import UserApiViewListing, UpdateUserApiView, PostUserApiView, LoginView, EnableDisableUserView

# LogoutView

app_name = "Users"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', UserApiViewListing.as_view(), name='Users'),

    path('add-user', PostUserApiView.as_view(), name='add-user/'),
    path('update-user', UpdateUserApiView.as_view(), name='update-user'),
    path('update-user/<int:pk>', UpdateUserApiView.as_view(), name='update-user'),
    path('login', LoginView.as_view(), name="login"),
    path('enable-disable/<int:pk>', EnableDisableUserView.as_view(), name='enable-disable-user')
    # path('logout', LogoutView.as_view(), name="logout")

]
