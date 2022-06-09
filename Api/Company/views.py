from django.db import IntegrityError

from Api.views import BaseApiView
from rest_framework import status
from django.core.exceptions import FieldError, ObjectDoesNotExist
from Api.Company.models import Company
from Api.Company.serializers import CompanySerializer, CompanyUpdateSerializer


class CompanyApiViewListing(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                company = Company.objects.get(id=pk)
                serializer = CompanySerializer(company)
                return self.send_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            company = Company.objects.all()
            serializer = CompanySerializer(company, many=True)
            return self.send_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(company), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Company.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Company doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class PostCompanyApiView(BaseApiView):
    def post(self, request):
        try:
            RequestedData = request.data
            serializer = CompanySerializer(data=RequestedData)
            if serializer.is_valid():
                serializer.save()
                return self.send_data_response(success=True, code=f'201', status_code=status.HTTP_201_CREATED,
                                               description='Company is created')
            return self.send_response(success=False, code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)

        except Company.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Company Model doesn't exists")
        except IntegrityError:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Email Already Exist")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class UpdateCompanyApiView(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                company = Company.objects.get(id=pk)
                serializer = CompanySerializer(company)
                return self.send_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            company = Company.objects.all()
            serializer = CompanySerializer(company, many=True)
            return self.send_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(company), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Company.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Company doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def put(self, request, pk=None):
        try:
            id1 = pk
            saved_company = Company.objects.get(pk=id1)
            data = request.data
            serializer = CompanyUpdateSerializer(instance=saved_company, data=data)
            if serializer.is_valid():
                serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='Company is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")
        except IntegrityError:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Email Already Exist")
        except Company.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Company Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def patch(self, request, pk=None):
        try:
            id1 = pk
            saved_company = Company.objects.get(id=id1)
            data = request.data
            serializer = CompanyUpdateSerializer(instance=saved_company, data=data, partial=True)
            if serializer.is_valid():
                saved_company = serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='Company is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")
        except Company.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Company doesn't exists")
        except IntegrityError:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Email Already Exist")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)
