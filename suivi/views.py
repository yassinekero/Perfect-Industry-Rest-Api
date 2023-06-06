
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produit
from .serializers import ProduitSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime





@api_view(['POST'])
def add_produit(request):
    token = request.COOKIES.get('jwt')
    if not token:
       raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')  
    produit = ProduitSerializer(data=request.data)
    if produit.is_valid():
        produit.save()
        return Response(produit.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET'])
def view_produit(request):

 
    if request.query_params:
        produit = Produit.objects.filter(**request.query_params.dict())
    else:
        produit = Produit.objects.all()
 

    if produit:
        serializer = ProduitSerializer(produit, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
def delete_produit(request, pk):
    token = request.COOKIES.get('jwt')
    if not token:
       raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    produit= get_object_or_404(Produit, pk=pk)
    produit.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def update_produit(request, pk):

    token = request.COOKIES.get('jwt')
    if not token:
       raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')  
    produit = Produit.objects.get(pk=pk)
    serializer = ProduitSerializer(produit, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)