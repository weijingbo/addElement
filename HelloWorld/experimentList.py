import json

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from HelloWorld.experimentDetail import getRegion, getConstellation, getStationByExpId, getConstellationGroup
from TestModel import models
from django.core import serializers
from django.utils import timezone


def login(request):
    body = json.loads(request.body.decode('utf-8'))
    account = body["account"]
    password = body["password"]
    user = models.User.objects.filter(account=account).get()
    print(user)
    if user.password == password:
        result = {
            "errorCode": 200,
            "userId": user.id,
            "authToken": 1
        }
    else:
        result = {
            "errorCode": 0,
            "errorMsg:": "密码不正确"
        }
    return JsonResponse(result, safe=False)


def register(request):
    body = json.loads(request.body.decode('utf-8'))
    account = body["account"]
    email = body["email"]
    password = body["password"]
    models.User.objects.create(account=account,
                               password=password,
                               email=email,
                               status=1)
    result = {
        "errorCode": 200,
    }
    return JsonResponse(result, safe=False)


@api_view(['GET'])
def getExperimentList(request, user_id):
    groups = models.UserGroup.objects.filter(userId=user_id)
    print(groups[0].userId)
    result = {
        "errorCode": 200,
        "data": list(groups)
    }
    return JsonResponse(result, safe=False)


def createGroup(request):
    body = json.loads(request.body.decode('utf-8'))
    groupName = body["groupName"]
    userId = body["userId"]
    models.UserGroup.objects.create(
        name=groupName,
        userId=userId
    )
    result = {
        "errorCode": 200,
        "errorMsg": "创建成功"
    }
    return JsonResponse(result, safe=False)

