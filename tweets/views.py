from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render

from .models import Tweet
# Create your views here.
def home_view(reques, *args,**kwargs):
    print(args,kwargs)
    return HttpResponse("<h1> Hello World<h1>")

def tweet_detail_view(reques,tweet_id,*args,**kwargs):
    """"
    Rest Api view
    consume bu js
    return json data
    """
    data={
        "id":tweet_id,
        "content": obj.content,
        #"image_path": obj.image.url
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