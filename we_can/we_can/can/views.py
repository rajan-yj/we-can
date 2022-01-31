from .models import Can, BinRequest
from we_can.user.models import User
from rest_framework import viewsets
from .serializers import CanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cans to be viewed or edited.
    """
    queryset = Can.objects.all()
    serializer_class = CanSerializer

class BinReported(APIView):
    
    def post(self, *args, **kwargs):
        user_id = kwargs.get('user_id', '')
        can_id = kwargs.get('can_id', '')
        can = Can.objects.get(pk=can_id)
        can.required = True
        can.save()
        return Response(can.required, status.HTTP_202_ACCEPTED)

class RequestBin(APIView):

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id', '')
        location = request.data
        user = User.objects.get(pk=user_id)

        new = BinRequest(user=user,location=location)
        new.save()
        return Response("created", status.HTTP_201_CREATED)
