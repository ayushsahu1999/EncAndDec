from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.forms import NewUser
from django.urls import reverse
from crypt import decode, encode
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def final(request):
    storage = get_messages(request)
    name = None
    for message in storage:
        name = message
        break
    print (type(name))
    name = str(name)

    n = str(encode(name))
    return render(request, 'first_app/final.html', {'answer': n})

def index(request):
    form = NewUser()

    if (request.method == 'POST'):
        form = NewUser(data=request.POST)

        if (form.is_valid()):
            form.save()
            # data = form.cleaned_data
            # field = data['line']


            # print (field)
            messages.add_message(request, messages.INFO, form.cleaned_data['line'])
            return HttpResponseRedirect('final')

        else:
            print ('Failed login')
            return HttpResponse('failed Input')
    else:
        form = NewUser()

    return render(request, 'first_app/index.html', {'form':form})
