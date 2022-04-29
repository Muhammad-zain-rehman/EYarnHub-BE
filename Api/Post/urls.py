from django.urls import path, include

from Api.Post.views import PostApiViewListing, AddPostApiView, UpdatePostApiView

app_name = "Posts"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', PostApiViewListing.as_view(), name='Posts'),

    path('add-post', AddPostApiView.as_view(), name='add-post/'),
    path('update-post', UpdatePostApiView.as_view(), name='update-post'),
    path('update-post/<int:pk>', UpdatePostApiView.as_view(), name='update-post')
]
