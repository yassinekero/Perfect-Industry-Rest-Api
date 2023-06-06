from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import Admin
import jwt, datetime
from rest_framework import status
from rest_framework.decorators import api_view




class AuthenticateView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')

        admin = Admin.objects.get(login = login)

        if admin is None:
            raise AuthenticationFailed('Wrong Admin Credentials')

        if not admin.check_password(password):
            raise AuthenticationFailed('Wrong Admin Credentials')

        payload = {
            'id': admin .id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        
        return response

@api_view(['GET'])
def view_produit(request):

    if request.query_params:
        produit = Admin.objects.filter(**request.query_params.dict())
    else:
        produit = Admin.objects.all()
 

    if produit:
        serializer = UserSerializer(produit, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class AdminView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        admin = Admin.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(admin)
        return Response(serializer.data)


class DeauthenticateView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
