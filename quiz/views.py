import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    if request.method == 'POST':  # when user click 'submit btn'
        total = []
        for q in question:
            select = request.POST[str(q.id)]
            choice = q.choice_set.all().values()
            for i in choice:
                if i['choice_text'] == select:
                    total.append(i['score'])
        return redirect(result, total=sum(total))
    return render(request, 'play.html', {'question': question})


def result(request, total):
    score = total
    return render(request, 'result.html', {'score':score})
