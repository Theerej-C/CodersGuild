from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user_registration(request,*args,**kwargs):
    return Response("Hello")