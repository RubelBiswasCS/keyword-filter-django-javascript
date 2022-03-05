from django.shortcuts import render
from .models import SearchHistory,Keyword
from django.http import JsonResponse,HttpResponse
from .models import User
import json
from .serializers import UserSerializer,SearchHistorySerializer,KeywordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
def search(request):
    # print('keywords')
    search_text = request.POST['search-text']
    keywords = search_text.split(' ')
    # print(keywords)
    # print(request.user)
    if request.method == 'POST':
        for keyword in keywords:
            try:
                kwd = Keyword.objects.get(name=keyword)
                kwd.count += 1
                history=SearchHistory.objects.create(user=request.user)
                kwd.search_history.add(history)
                history.save()
                kwd.save()
            except:
                kwd = Keyword.objects.create(name=keyword,count=1)
                history=SearchHistory.objects.create(user=request.user)
                kwd.search_history.add(history)
                history.save()
                kwd.save()
        context = {
            'search_text': search_text,
        }
        return render(request, template_name='search-feed.html',context=context)
    return HttpResponse("Unexpected request method")

def analyzer(request):
    # keywords=SearchHistory.objects.all()
    # users = User.objects.all()
    # # kkeywords = [json.dumps(keyword) for keyword in keywords]
    # print(keywords)
    # context={
    #     "keywords":list(keywords.values()),
    #     "users":list(users.values('id','username')),
    # }
    #return JsonResponse({'data':list(keywords.values()),'users':list(users.values('id','username'))})
    return render(request,template_name='keyword-analyzer.html')

class DataList(APIView):
    def get(self,request):
        keywords=Keyword.objects.all()
        keywords = KeywordSerializer(keywords,many=True)
        search_history=SearchHistory.objects.all()
        search_history = SearchHistorySerializer(search_history,many=True)
        users = User.objects.all()
        print(users)
        users = UserSerializer(users,many=True)
        data = [keywords.data,users.data,search_history.data]
        return Response(data,status=status.HTTP_200_OK)

