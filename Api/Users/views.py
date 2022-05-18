from django.db import IntegrityError
from django.contrib.auth import logout, authenticate
from Api.views import BaseApiView
from rest_framework import status
from django.core.exceptions import FieldError, ObjectDoesNotExist
from Api.Users.models import User
from Api.Users.serializers import UserSerializer, UserUpdateSerializer, AuthenticationSerializer


class LoginView(BaseApiView):
    """LOGIN View"""

    # authentication_classes = ()
    # permission_classes = ()

    def post(self, request, pk=None):
        try:
            serializer = AuthenticationSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                user = authenticate(request, email=email, password=password)
                if user:
                    if user.is_active:
                        oauth_token = self.get_oauth_token(email, password)
                        if 'access_token' in oauth_token:
                            serializer = UserSerializer(User.objects.get(id=user.id))
                            user_data = serializer.data
                            user_data['access_data'] = oauth_token.get('access_token')
                            user_data['refresh_token'] = oauth_token.get('refresh_token')
                            return self.send_response(
                                success=True, status_code=status.HTTP_200_OK, payload=user_data,
                                code=f'200',
                                description='You are logged In',
                                log_description=f'User {user_data["email"]}.with id.{user_data["id"]}. has just logged in')
                        else:
                            return self.send_response(description="Something went wrong with oauth token generation",
                                                      code=f'500')
                    else:
                        description = 'Your account is blocked or deleted.'
                        return self.send_response(success=False,
                                                  code=f'422',
                                                  status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                                  payload={},
                                                  description=description)
                else:
                    return self.send_response(
                        success=False,
                        code=f'422',
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        payload={}, description='Email or password is incorrect.'
                    )
            else:
                return self.send_response(
                    success=False,
                    code='422',
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    description=serializer.errors
                )
        except Exception as e:
            return self.send_response(code=f'500',
                                      description=e)


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
                serializer = UserUpdateSerializer(user)
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
