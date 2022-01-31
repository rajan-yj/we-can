from .models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostPoints(APIView):
    
    def post(self, *args, **kwargs):
        user_id = kwargs.get('user_id', '')
        can_id = kwargs.get('can_id', '')
        user = User.objects.get(pk=user_id)
        user.score += 1
        user.save()
        return Response(user.score, status.HTTP_202_ACCEPTED)

class Register(APIView):

    def post(self, *args, ** kwargs):
        name = kwargs.get('name', '')
        user = User(name=name)
        try:
            user.save()
        except:
            return Response("Name Already Exist", status.HTTP_406_NOT_ACCEPTABLE)
        return Response(user.name, status.HTTP_201_CREATED)

class KarmaBoard(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        userlist = User.objects.all().order_by('-score')[:10]
        res = []
        for i in range(len(userlist)):
            a = {}
            a['rank'] = i+1
            a['name'] = userlist[i].name
            a['score'] = userlist[i].score
            res.append(a)
        res = {"data": res}
        return Response(res, status.HTTP_200_OK)