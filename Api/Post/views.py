from django.db import IntegrityError

from Api.views import BaseApiView
from rest_framework import status
from django.core.exceptions import FieldError, ObjectDoesNotExist
from Api.Post.models import Posts
from Api.Post.serializers import PostSerializer


class PostApiViewListing(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                post = Posts.objects.get(id=pk)
                serializer = PostSerializer(post)
                return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            post = Posts.objects.all()
            serializer = PostSerializer(post, many=True)
            return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(post), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No post matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Posts.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Post doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class AddPostApiView(BaseApiView):
    def post(self, request):
        try:
            RequestedData = request.data
            serializer = PostSerializer(data=RequestedData)
            if serializer.is_valid():
                save_post = serializer.save()
                return self.send_data_response(success=True, code=f'201', status_code=status.HTTP_201_CREATED,
                                               description='Post is created')
            return self.send_response(success=False, code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)

        except Posts.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Post Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)


class UpdatePostApiView(BaseApiView):
    def get(self, request, pk=None):
        try:
            if pk is not None:
                post = Posts.objects.get(id=pk)
                serializer = UpdatePostSerializer(post)
                return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                               code='',
                                               description='Details of serializer', log_description='')
            post = Posts.objects.all()
            serializer = UpdatePostSerializer(post, many=True)
            return self.send_data_response(success=True, status_code=status.HTTP_200_OK, payload=serializer.data,
                                           code='',
                                           description='Details of serializer', count=len(post), log_description='')
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No post matches the given query.")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Posts.DoesNotExist:
            return self.send_response(code='', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Post doesn't exists")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def put(self, request, pk=None):
        try:
            id1 = pk
            save_post = Posts.objects.get(id=id1)
            data = request.data
            serializer = PostSerializer(instance=save_post, data=data)
            if serializer.is_valid():
                serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='Post is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Post matches the given query.")
        except Posts.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Post Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500', description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)

    def patch(self, request, pk=None):
        try:
            id1 = pk
            save_post = Posts.objects.get(id=id1)
            data = request.data
            serializer = PostSerializer(instance=save_post, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return self.send_response(success=True, code=f'200', status_code=status.HTTP_200_OK,
                                          description='Post is updated')
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description=serializer.errors)
        except ObjectDoesNotExist:
            return self.send_response(code='422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="No Post matches the given query.")
        except Posts.DoesNotExist:
            return self.send_response(code=f'422', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                      description="Post Model doesn't exists")
        except FieldError:
            return self.send_response(code=f'500',
                                      description="Cannot resolve keyword given in 'order_by' into field")
        except Exception as e:
            return self.send_response(code=f'500', description=e)