from rest_framework.views import APIView
from rest_framework import status
from rest_framework.status import is_server_error
from rest_framework.response import Response

from EyarnHub import settings


class BaseApiView(APIView):
    """BASE CLASS OF ALL API VIEWS """

    def send_response(self, success=False, code='', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, payload={},
                      description='', exception=None, count=0, log_description=""):
        """
        GENERATE RESPONSE
        :param log_description:
        :param count:
        :param success: it's a boolean value, tell us either call is successfull or not
        :param code: string type status code
        :param status_code: int TypeHTTP Status Code
        :param payload: list data generate forrespective api call
        :param description: string type for any description
        :param exception: str type exception
        :rtype: dict.
        """
        if not success and is_server_error(status_code):
            if settings.DEBUG:
                description = f'error Message: {description}'
            else:
                description = 'Internal Server Error'
        return Response(
            data={'success': success, 'code': code, 'payload': payload, 'description': description, 'count': count},
            status=status_code
        )

    def send_data_response(self, success=False, code='', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, payload={},
                           description='', exception=None, count=0, log_description=""):
        """
        GENERATE RESPONSE
        :param log_description:
        :param count:
        :param success: it's a boolean value, tell us either call is successfull or not
        :param code: string type status code
        :param status_code: int TypeHTTP Status Code
        :param payload: list data generate forrespective api call
        :param description: string type for any description
        :param exception: str type exception
        :rtype: dict.
        """
        if not success and is_server_error(status_code):
            if settings.DEBUG:
                description = f'error Message: {description}'
            else:
                description = 'Internal Server Error'
        return Response(
            data={'data': {'success': success, 'code': code, 'payload': payload, 'description': description, 'count': count}},
            status=status_code
        )
