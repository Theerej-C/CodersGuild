from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def problem_run(request,*args,**kwargs):
    return Response("Hello")
