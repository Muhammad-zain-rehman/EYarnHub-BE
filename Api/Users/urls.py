from django.urls import path, include

from Api.Users.views import UserApiViewListing,UpdateUserApiView,PostUserApiView

app_name = "Users"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', UserApiViewListing.as_view(), name='Users'),

    path('add-user', PostUserApiView.as_view(), name='add-user/'),
    path('update-user', UpdateUserApiView.as_view(), name='update-user'),
    path('update-user/<int:pk>', UpdateUserApiView.as_view(), name='update-user')
]
