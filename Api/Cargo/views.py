from django.db import IntegrityError

from Api.views import BaseApiView
from rest_framework import status
from django.core.exceptions import FieldError, ObjectDoesNotExist
from Api.Cargo.models import Cargo
from Api.Cargo.serializers import CargoSerializer


class CargoCompanyApiViewListing(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                company = Cargo.objects.get(id=pk)
                serializer = CargoSerializer(company)
                return self.send_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                          code='',
                                          description='Details of serializer', log_description='')
            cargoObjects = Cargo.objects.all()
            serializer = CargoSerializer(cargoObjects, many=True)
            return self.send_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                      code='',
                                      description='Details of serializer', count=len(cargoObjects), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Cargo.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Cargo Company doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class PostCargoCompanyApiView(BaseApiView):
    def post(self, request):
        try:
            RequestedData = request.data
            serializer = CargoSerializer(data=RequestedData)
            if serializer.is_valid():
                serializer.save()
                return self.send_data_response(success=True, code=f'201', status_code=status.HTTP_201_CREATED,
                                               description='Cargo Company is created')
            return self.send_response(success=False, code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)

        except Cargo.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Cargo Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class UpdateCargoCompanyApiView(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                company = Cargo.objects.get(id=pk)
                serializer = CargoSerializer(company)
                return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            company = Cargo.objects.all()
            serializer = CargoSerializer(company, many=True)
            return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(company), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Cargo.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Cargo Company doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def put(self, request, pk=None):
        try:
            id1 = pk
            saved_company = Cargo.objects.get(id=id1)
            data = request.data
            serializer = CargoSerializer(instance=saved_company, data=data)
            if serializer.is_valid():
                serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='Cargo Company is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Company matches the given query.")

        except Cargo.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Cargo Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def patch(self, request, pk=None):
        try:
            id1 = pk
            saved_company = Cargo.objects.get(id=id1)
            data = request.data
            serializer = CargoSerializer(instance=saved_company, data=data, partial=True)
            if serializer.is_valid():
                saved_company = serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='Cargo Company is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Cargo Company matches the given query.")
        except Cargo.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Cargo doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class EnableDisableCargoViewView(BaseApiView):
    def get(self, request, pk=None):
        try:
            obj = Cargo.objects.get(id=pk)
            obj.is_active = not obj.is_active
            obj.save()
            if obj.is_active:
                return self.send_response(success=True,
                                          status_code=status.HTTP_200_OK,
                                          code='',
                                          description='Company enabled Successfully!'
                                          )
            else:
                return self.send_response(success=True,
                                          code='',
                                          status_code=status.HTTP_200_OK,
                                          description='Company disabled Successfully!'
                                          )
        except Exception as e:
            return self.send_response(success=False,
                                      code=status.HTTP_400_BAD_REQUEST,
                                      description='Compnay does not exist')
