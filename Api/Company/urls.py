from django.urls import path, include

from Api.Company.views import CompanyApiViewListing, PostCompanyApiView,UpdateCompanyApiView

app_name = "Company"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', CompanyApiViewListing.as_view(), name='Companies'),
    # path('companies/<int:pk>', CompanyApiViewListing.as_view(), name='Companies'),

    path('add-company', PostCompanyApiView.as_view(), name='add-company/'),
    path('update-company', UpdateCompanyApiView.as_view(), name='update-company'),
    path('update-company/<int:pk>', UpdateCompanyApiView.as_view(), name='update-company')

]
