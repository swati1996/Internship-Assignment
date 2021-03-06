from django.contrib.auth.models import User
from rest_framework import viewsets
from assignment_1.serializers import UserSerializer
from . models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
