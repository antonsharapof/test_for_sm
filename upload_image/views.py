from pytz import unicode
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import  MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import time
from .serializer import ImageSerializer


"""Первый способ без моделей и сериализаторов"""
@api_view(['POST'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def first_way(request):
    answer = []
    for file in request.FILES.getlist('image'):
        if file.size < 200000 and file.content_type.split('/')[0] == 'image':
            name = ''.join(['media/', str(time.time()), '_', file.name])
            with open(name, 'wb') as r:
                r.write(file.read())
            answer.append("{} uploaded".format(file.name))
        else:
            answer.append("{} is not image or size > 20kB".format(file.name))
    return Response({'received data': answer})


"""Второй способ с моделями и сереализаторами"""
class SecondWay(viewsets.ModelViewSet):

    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        images = request.data
        answer = []
        for image in images.getlist('image'):
            serializer = self.serializer_class(data={'image': image})
            if serializer.is_valid():
                serializer.save()
                answer.append('{} uploaded'.format(image.name))
            else:
                answer.append('{} not uploaded. {}'.format(image.name, serializer.errors))

        return Response({'Answer': answer})

