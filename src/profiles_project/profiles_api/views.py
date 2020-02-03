from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models
class HelloApiView(APIView):
    """Test API View."""

    serializer_class  = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview= [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "xin chao {0}",format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_404_BAD_Request)

    def put(self, request,pk = None):
        """Handle updating an object."""
        return Response({'method':'put'})


    def patch(self, request,pk = None):
        """patch request, only updates fields provided in the request."""
        return Response({'method':'patch'})

    def delete(self, request,pk = None):
        """Deletes and object."""
        return Response({'method':'delete'})
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return a hello message."""

        a_viewset={
        'User action (lits,create,retrieve,update,partial_update)',
        'automatically maps to URLs using Routers',
        'Provides more functions with less code.'
        }
        return Response({'message':'hello','a_viewset': a_viewset})
    def create(self,request):
        """create a new hello message."""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "xin chao {0}",format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_404_BAD_Request)
    def retrieve(self, request,pk = None):
        """Handle getting an object by its ID."""

        return Response({'http_method':'GET'})
    def update(self, request,pk = None):
        """Handle updating an object."""
        return Response({'method':'PUT'})
    def partial_update(self, request,pk = None):
        """Handle updating part an object."""
        return Response({'method':'PATCH'})
    def destroy(self, request,pk = None):
        """Handle removing an object."""
        return Response({'method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.Userprofile.objects.all()
