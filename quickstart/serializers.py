from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from dj198.polls.models import Items
from polls.models import Items

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Items
		fields = ('name','email','address')