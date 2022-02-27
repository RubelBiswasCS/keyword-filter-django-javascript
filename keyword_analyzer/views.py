from django.shortcuts import render
from .models import SearchHistory
from django.http import JsonResponse,HttpResponse
from .models import User
import json
from .serializers import UserSerializer,SearchHistorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

        keywords=SearchHistory.objects.all()
        keywords = SearchHistorySerializer(keywords,many=True)
        users = User.objects.all()
        print(users)
        users = UserSerializer(users,many=True)
        data = [keywords.data,users.data]
        return Response(data,status=status.HTTP_200_OK)

