from django.urls import path, include

from Api.Company import urls
app_name = "Api"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('company/', include('Api.Company.urls')),
    path('cargo/', include('Api.Cargo.urls')),
    path('users/', include('Api.Users.urls')),
    path('posts/', include('Api.Post.urls'))
]
