import requests
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.status import is_server_error
from rest_framework.response import Response
from requests.auth import HTTPBasicAuth

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
            data={'data': {'success': success, 'code': code, 'payload': payload, 'description': description,
                           'count': count}},
            status=status_code
        )

    @staticmethod
    def get_oauth_token(email="", password="", grant_type='password'):
        try:
            url = settings.AUTHORIZATION_SERVER_URL
            # it will be seems like url ='http://192.168.18.16:8000/api/oauth/token/'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'username': email,
                'password': password,
                'grant_type': grant_type
            }
            auth = HTTPBasicAuth(
                settings.OAUTH_CLIENT_ID,
                settings.OAUTH_CLIENT_SECRET
            )
            response = requests.post(
                url=url,
                headers=headers,
                data=data,
                auth=auth
            )
            if response.ok:
                json_response = response.json()
                return {
                    'access_token': json_response.get('access_token', ''),
                    'refresh_token': json_response.get('refresh_token', '')
                }
            else:
                return {'error': response.json().get('error')}
        except Exception as e:
            # fixme: Add logger to log this exception
            return {'exception': str(e)}

    @staticmethod
    def revoke_oauth_token(token):
        try:
            url = settings.REVOKE_TOKEN_URL
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'token': token,
                'client_secret': settings.OAUTH_CLIENT_SECRET,
                'client_id': settings.OAUTH_CLIENT_ID
            }
            response = requests.post(
                url=url,
                headers=headers,
                data=data
            )
            if response.ok:
                return True
            else:
                return False
        except Exception:
            # fixme: Add logger to log this exception
            return False

