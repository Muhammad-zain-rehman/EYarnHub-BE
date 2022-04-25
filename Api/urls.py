from django.urls import path, include

from Api.Company import urls
app_name = "Api"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('company/', include('Api.Company.urls')),
]
