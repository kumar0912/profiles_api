from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request, format = None):
        """Returns a list of APIView features"""
        an_api = [
        'Uses HTTP methods as function(get,post,patch,put,delete)',
        'Is similar to a traditional django view',
        'Givs you the most control over he applicaion logic',
        'Is maaped manually to the URLs',
        ]
        """Returning a dictionary"""
        return Response({'message':'Hello','an_api':an_api})

    def post(self,request):
         """Create a hello message with our name"""
         serializer = self.serializer_class(data = request.data)
         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             message = 'Hello '+name
             return Response({'message':message})
         else:
             return Response(
             serializer.errors,
             status = status.HTTP_400_BAD_REQUEST
             )

    def put(self,request,pk=None):
        """HAndle updating a complete object or can be called to replace"""
        return Response({'method':'PUT'})

    def patch(self,request ,pk=None):
        """Handle partial upadte of an object"""
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        a_viewset = [
            'Uses actions (lisr,create,retrieve,...)',
            'Provides more functionality with less code',
            'Automatocally maps to the URLs',
            ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello meassage"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello '+name
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its iD"""
        return Response({'http_method':'GET'})

    def partial_update(self,request,pk = None):
        """handle partial update of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http-method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    """To add Filters to api"""
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authenticaton tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
