# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from __future__ import print_function
import json
import os
from watson_developer_cloud import ConversationV1

#########################
# message
#########################


# Create your views here.

def home_view(request):
    print("anjali")
    conversation = ConversationV1(
        username='bd7d4fc4-c4dd-4972-91a6-d153655d8d18',
        password='gQDNFUPImSQs',
        version='2017-04-21')

    # replace with your own workspace_id
    workspace_id = '8f12d21e-c722-4e25-a94a-aae6e5eafd3d'
    if os.getenv("conversation_workspace_id") is not None:
        workspace_id = os.getenv("conversation_workspace_id")

    response = conversation.message(workspace_id=workspace_id, input={
        'text':request.POST.get("input")})
    # print(response)

    detail=(response.items()[2][1]).items()[0][1][0]
    if detail is None:
        detail="Sorry , for any additional details visit the website"
    data={"output":detail}

    return JsonResponse(data)

def h_view(request):
    return render(request,"somechatbox.html",{})
    # sches=json.dumps(response, indent=2)
    # data={"text"}
    # return JsonResponse(data)
