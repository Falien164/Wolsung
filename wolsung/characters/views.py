from django.http import JsonResponse, HttpResponse
from .models import Character
from .serializers import CharacterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index2(request):
    return HttpResponse("Test.")


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
