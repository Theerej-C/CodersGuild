from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .database import user_collection
from rest_framework.permissions import AllowAny
from .encoding import generate_access_token, generate_refresh_token
from rest_framework import exceptions

params = ["email","user_name","password"]


@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request,*args,**kwargs):
    data = request.data
    for n in params:
        if n not in data.keys():
            return Response("The "+n+" field is required")
    if user_collection.find_one({"user_name":data.get("user_name")}):
        return Response("User Already exsist")
    user_name = data.get("user_name")
    email = data.get("email")
    password = data.get("password")
    count = user_collection.estimated_document_count()
    user_data = {
        "_id":count+1,
        "user_name":user_name,
        "email":email,
        "password":password,
        "problem_solved_count":None,
        "solved_problem_list":None
    }
    db_code = user_collection.insert_one(user_data)
    token = generate_access_token(user_data)
    return Response({"access_token":token})



@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request,*args,**kwargs):
    username = request.data.get('user_name')
    password = request.data.get('password')
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')
    user = user_collection.find_one({"user_name":username})
    if not user:
        raise exceptions.AuthenticationFailed('user not found')
    if user["password"]!=password:
        raise exceptions.AuthenticationFailed('wrong password')
    token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    response = Response()
    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        "access_token":token,
        "user": username
    }
    return response

@api_view(['GET'])
def testing_view(request):
    return Response("Testing")