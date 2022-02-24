from django.shortcuts import render
from .models import SearchHistory
from django.shortcuts import HttpResponse

def search(request):
    print('keywords')
    search_text = request.POST['search-text']
    keywords = search_text.split(' ')
    print(keywords)
    print(request.user)
    if request.method == 'POST':
        for keyword in keywords:
            SearchHistory.objects.create(user=request.user,keyword=keyword)
        context = {
            'search_text': search_text,
        }
        return render(request, template_name='search-feed.html',context=context)
    return HttpResponse("Unexpected request method")

def analyzer(request):
    keywords=SearchHistory.objects.all()
    context={
        "keywords":keywords,
    }
    return render(request,template_name='keyword-analyzer.html',context=context)
