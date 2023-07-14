from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 撰寫邏輯


def index(request):
    return HttpResponse("django test 2")

