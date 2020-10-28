from django.contrib import admin

# Register your models here.
from .models import Tweet # we import Tweet with all the enteries we had done uptill

class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__','user']
    search_fields = ['content','user__username','user__email']
    class Meta:
        model=Tweet

admin.site.register(Tweet,TweetAdmin) # this ensures the Tweet is registered in admin page