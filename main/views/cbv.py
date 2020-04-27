from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import User, Twit
from main.serializers import UserSerializer, TwitSerializer

class TwitList(generics.ListCreateAPIView):
    queryset = Twit.objects.all()
    serializer_class = TwitSerializer
    permission_classes = (IsAuthenticated,)


class TwitDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Twit.objects.all()
    serializer_class = TwitSerializer
    permission_classes = (IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserTwit(APIView):
    def get(self, request, country_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        people = User.objects.filter(country_id=country_id)
        # print(people.get(0))
        serializer = UserSerializer(people, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TwitUser(APIView):
    def get(self, request, country_id):
        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        people = Twit.objects.filter(country_id=country_id)
        # print(people.get(0))
        serializer = TwitSerializer(people, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = TwitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


