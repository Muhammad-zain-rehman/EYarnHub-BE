from django.db import IntegrityError

from Api.views import BaseApiView
from rest_framework import status
from django.core.exceptions import FieldError, ObjectDoesNotExist
from Api.Users.models import User
from Api.Users.serializers import UserSerializer, UserUpdateSerializer


class UserApiViewListing(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                user = User.objects.get(id=pk)
                serializer = UserSerializer(user)
                return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            company = User.objects.all()
            serializer = UserSerializer(company, many=True)
            return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(company), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No user matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except User.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="User doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class PostUserApiView(BaseApiView):
    def post(self, request):
        try:
            RequestedData = request.data
            serializer = UserSerializer(data=RequestedData)
            if serializer.is_valid():
                user_save = serializer.save()
                return self.send_data_response(success=True, code=f'201', status_code=status.HTTP_201_CREATED,
                                               description='User is created')
            return self.send_response(success=False, code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)

        except User.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="User Model doesn't exists")
        except IntegrityError:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Email Already Exist")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class UpdateUserApiView(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                user = User.objects.get(id=pk)
                serializer = UpdateCompanyApiView(user)
                return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(user), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No User matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except User.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="User doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def put(self, request, pk=None):
        try:
            id1 = pk
            saved_user = User.objects.get(id=id1)
            data = request.data
            serializer = UserUpdateSerializer(instance=saved_user, data=data)
            if serializer.is_valid():
                serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='User is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No User matches the given query.")
        except IntegrityError:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Email Already Exist")
        except User.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="User Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def patch(self, request, pk=None):
        try:
            id1 = pk
            saved_user = User.objects.get(id=id1)
            data = request.data
            serializer = UserUpdateSerializer(instance=saved_user, data=data, partial=True)
            if serializer.is_valid():
                user_saved = serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='User is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No User matches the given query.")
        except User.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="User doesn't exists")
        except IntegrityError:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Email Already Exist")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)
