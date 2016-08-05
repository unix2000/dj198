# from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from dj198.quickstart.serializers import UserSerializer, GroupSerializer, ItemsSerializer
#from dj198.polls.models import Items
from quickstart.serializers import UserSerializer, GroupSerializer, ItemsSerializer
from polls.models import Items

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ItemsViewSet(viewsets.ModelViewSet):
	queryset = Items.objects.all()
	serializer_class = ItemsSerializer
