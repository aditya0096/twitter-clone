import random
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render,redirect

from .forms import TweetForm
from .models import Tweet
# Create your views here.
def home_view(request, *args,**kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    print("next_url",next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        #do other form related topics
        obj.save()
        form = TweetForm()
    return render(request, 'components/forms.html', context={"form": form})

def tweet_list_view(request,*args,**kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes":random.randint(0,123)} for x in qs]
    data = {
        "isUser": False,
        "response":tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request,tweet_id,*args,**kwargs):
    """"
    Rest Api view
    consume bu js
    return json data
    """
    data={
        "id":tweet_id,
    }
    status=200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']= obj.content
    except:
        data['message']= "Not Found"
        status=404
    return JsonResponse(data,status=status)
    #return HttpResponse(f"<h1> Hello {tweet_id}-{obj.content}<h1>")