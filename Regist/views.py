from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.db.models import Q
from Regist.models import UserInformation, PushData



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    # get input
    userphone = request.GET['phoneNumber']
    userpasswd = request.GET['userPassword']
    response = UserInformation.objects.get(phone=userphone)
    # return HttpResponse("login success!")
    if response.password == userpasswd:
        res = {"errno": 0, "errmsg": "login successed!","data": ""}
    else:
        res = {"errno": 1, "errmsg": "login failed!"}
        # return HttpResponse("login fail!!")
    role = response.roles
    UID = response.uid
    data = {"UID": UID, "roles": role}
    res["data"] = data
    json_res = json.dumps(res)
    res_load = json.loads(json_res)
    # print res_load
    return HttpResponse(json_res)


def search(request):
    userid = request.GET['userId']
    searchmonth = request.GET['month']
    # searchdate = request.GET['dateId']
    date_list = []
    response_list = PushData.objects.filter(Q(uid=userid), Q(month=searchmonth))
    for res in response_list:
        date_list.append(res.date_info)
    data = {"UID": userid, "month": searchmonth, "dates": date_list}
    res = {"errno": 0, "errmsg": "search successed!", "data": data}
    json_res = json.dumps(res)
    res_load = json.loads(json_res)
    # print res_load
    return HttpResponse(json_res)
    # return HttpResponse("hello search")


def push(request):
    userid = request.GET['userId']
    pushdate = request.GET['date']
    pushmonth = request.GET['month']
    return HttpResponse("push success!")


def searchPush(request):
    return HttpResponse("push success!")


def confirmPush(request):
    return HttpResponse("push success!")