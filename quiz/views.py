import datetime

from django.http import HttpResponse
from django.shortcuts import render
from quiz.models import Question


# Create your views here.
# 撰寫邏輯


def index(request):
    return HttpResponse("django test 2")


# Homepage

def homepage(request):
    now = datetime.datetime.now()
    context = {'now': now}
    return render(request, 'homepage.html', context)


def play(request):
    question = Question.objects.all()
    return render(request, 'play.html', {'question': question})
