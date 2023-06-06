from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Demande
from .serializers import DemandeSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


@api_view(['POST'])
def add_demande_contact(request):

    demande = DemandeSerializer(data=request.data)
    if demande.is_valid():
        demande.save()
        return Response(demande.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET'])
def view_demande_contact(request):

    token = request.COOKIES.get('jwt')
    if not token:
       raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    if request.query_params:
        demande = Demande.objects.filter(**request.query_params.dict())
    else:
        demande = Demande.objects.all()
 
    
    if demande:
        serializer = DemandeSerializer(demande, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['DELETE'])
def delete_demande(request, pk):
    token = request.COOKIES.get('jwt')
    if not token:
       raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')   
    demande= get_object_or_404(Demande, pk=pk)
    demande.delete()
    return Response(status=status.HTTP_202_ACCEPTED)