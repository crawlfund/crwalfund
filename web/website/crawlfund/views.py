from django.shortcuts import render
from django.http import HttpResponse
from crawlfund.models import Question
from django.template import RequestContext,loader
from django.shortcuts import render
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list':latest_question_list}
    return render(request,'crawlfund/index.html',context)
    return HttpResponse(template.render(context))
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'detail/detail.html',{'question':question})
def results(request,question_id):
    response = "You're looking at the result of the question %s"
    return HttpResponse(response % question_id)
def vote(response,question_id):
    return HttpResponse("You're voting on question %s. " % question_id)
