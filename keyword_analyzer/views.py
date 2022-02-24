from django.shortcuts import render
from .models import SearchHistory
from django.shortcuts import HttpResponse

def search(request):
    print('keywords')
    if request.method == 'POST':
        context = {
            'data': 'data',
        }
        return render(request, template_name='home.html',context=context)
    return HttpResponse("response")