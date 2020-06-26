from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse

from .models import Question, Choice

#Get Questions and Display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #pass in as dictionary
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

#Show question and choice
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', { 'question': question})

#Get question and display results
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html',{ 'question': question})

def vote(request,question_id):
    question= get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question form
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message': "You did not select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Redirect to results
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))