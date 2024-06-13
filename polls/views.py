from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from . import models
from django.template import loader

def index(req):
    latest_questions = models.Question.objects.order_by("-pub_date")[:5]
    ctx={
        "latest_questions":latest_questions
    }
    return render(request=req,context=ctx,template_name="polls/index.html")

def details(req,question_id):
    try:
        question = models.Question.objects.get(id=question_id)
    except models.Question.DoesNotExist:
        return Http404(f"Question with id {question_id} not found")
    return render(request=req,context={"question":question},template_name="polls/detail.html")
    # return HttpResponse(f"you are looking at question details with id{question_id}")


def result(req,question_id):
    # question = models.Question.objects.get(id=question_id)
    # ctx={"question":question}
    # return HttpResponse(f"you are looking at question result with id{question_id}")
    question = get_object_or_404(models.Question,pk=question_id);
    return 


def votes(req,question_id):
    return HttpResponse(f"you are looking at question with id:{question_id}")