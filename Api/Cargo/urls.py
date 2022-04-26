from django.urls import path, include

from Api.Cargo.views import CargoCompanyApiViewListing, PostCargoCompanyApiView, UpdateCargoCompanyApiView

app_name = "Cargo"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', CargoCompanyApiViewListing.as_view(), name='Cargo_Companies'),

    path('add-cargo-company', PostCargoCompanyApiView.as_view(), name='add-cargo=company/'),
    path('update-cargo-company', UpdateCargoCompanyApiView.as_view(), name='update-cargo-company'),
    path('update-cargo-company/<int:pk>', UpdateCargoCompanyApiView.as_view(), name='update-cargo-company')

]
