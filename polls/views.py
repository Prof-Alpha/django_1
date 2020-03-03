from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Choices, Questions
from django.urls import reverse

def index(request):
    qu = Questions.objects.all()
    #cho = qu.choices_set.all()
    send = {
        'qu':qu,
        #'cho':cho,
    }
    return render(request, 'polls/index.html', send)

def results(request, qu_num):
    qu = get_object_or_404(Questions, pk=qu_num)
    return render(request, 'polls/results.html', {'qu': qu})

def vote(request, qu_number):
    ab = Choices.objects.get(pk=request.POST['votee'])
    ab.vote += 1
    ab.save()
    #return render(request, 'polls/results.html')
    #     return HttpResponseRedirect(reverse('results'))
    return HttpResponseRedirect(reverse('results', args=(qu_number,)))