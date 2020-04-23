from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our api view"""
    name = serializers.CharField(max_length=100)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    """We use this meta class to configure our serializer
    to a specific model"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password') 
        extra_kwargs = {
          'password':{
              'write_only':True,
              'style':{'input_type':'padsword'}
          }
        }
    def create(self,validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user (
          email = validated_data['email'],
          name = validated_data['name'],
          password = validated_data['password'],
        )
        return user
