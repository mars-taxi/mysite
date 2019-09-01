from django.shortcuts import render

from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.


def index(request):
    return HttpResponse("This is a poll index. Try it out!!!")


def detail(request, question_id):
    response = "You are looking at the question %s:\n %s\n %s"
    q = Question.objects.get(id=question_id)
    question_text = q.question_text
    question_pub_date = q.pub_date
    return HttpResponse(response % (question_id, question_text, question_pub_date))


def results(request, question_id):
    response = "The result of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're voting on question %s"
    return HttpResponse(response % question_id)
