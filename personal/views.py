from django.http import HttpResponse, Http404
from django.shortcuts import render
from personal.models import Questions, classOne, to_do


# Create your views here.

def main_page(request):
    obj_1 = Questions.objects.all()
    contextt = {
        'key_1':obj_1,
    }
    return render(request, 'personal/home.html', contextt)

# --------- CRUD TEST ------------------------
def crud_test(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        # email = request.POST['email']
        # password = request.POST['password']
        obj_1 = classOne(title=firstname, question=lastname, priority='L')
        obj_1.save()

    return render(request, 'crud_test.html')
#---------------------------------------------------
def test(request):
    if request.method == 'POST':
        taskss = request.POST['taskss']
        qq = to_do(task=taskss)
        qq.save()

    obj = to_do.objects.all()
    send = {'items':obj, }
    return render(request, 'test.html', send)
#---------------------------------------------------
def details(request, qid):
    try:
        qu = to_do.objects.get(pk=qid)
    except to_do.DoesNotExist:
        raise Http404('YOOOOOOOOOKKKHHH')
    send = {
        'item':qu,
    }
    return render(request, 'test_2.html', send)
 
 