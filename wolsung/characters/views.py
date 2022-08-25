from django.http import JsonResponse, HttpResponse
from .models import Character
from .serializers import CharacterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def add_character(request):
    if request.method == "POST":
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_characters(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return JsonResponse({'characters': serializer.data})


@api_view(['GET'])
def get_character(request, id):
    try:
        char = Character.objects.get(pk=id)
    except Character.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializers = CharacterSerializer(char)
    return Response(serializers.data)
