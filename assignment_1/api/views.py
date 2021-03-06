from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from assignment_1.models import User
from assignment_1.api.serializers import RegistrationSerializer

@api_view(['post',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "registration successful"
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
        else:
            data = serializer.errors
        return Response(data)
