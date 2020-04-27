from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import User,Twit
from main.serializers import UserSerializer, TwitSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        countries = User.objects.all()
        serializer = UserSerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def twit_list(request):
    if request.method == 'GET':
        countries = Twit.objects.all()
        serializer = TwitSerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TwitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, country_id):
    try:
        user = User.objects.get(id=country_id)
    except User.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        user.delete()
        return Response({'deleted': True})

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def twit_detail(request, country_id):
    try:
        twit = Twit.objects.get(id=country_id)
    except Twit.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = TwitSerializer(twit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TwitSerializer(instance=twit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        twit.delete()
        return Response({'deleted': True})

