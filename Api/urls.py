import oauth2_provider.views as oauth2_views
from django.urls import path, include, re_path
from Api.Company import urls
app_name = "Api"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    re_path(r'^oauth/outhorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    re_path(r'^oauth/token/$', oauth2_views.TokenView.as_view(),name="token"),
    re_path(r'oauth/revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke_token"),
    path('company/', include('Api.Company.urls')),
    path('company/<int:pk>', include('Api.Company.urls')),

    path('cargo/', include('Api.Cargo.urls')),
    path('cargo/<int:pk>', include('Api.Cargo.urls')),

    path('users/', include('Api.Users.urls')),
    path('posts/', include('Api.Post.urls'))
]
