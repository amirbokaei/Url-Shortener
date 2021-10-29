from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django import views
import uuid


# Create your views here.
class shortetView(views.View):
    def get(self, request):
        form = ShortRequestForm()
        return render(request, 'url-short/request.html', {'form':form})

    def post(self, request):
        form = ShortRequestForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            try:
                old = url_shorten.objects.get(orgin_url=url)
                return render(request, 'url-short/massage.html', {'short_url':old.short_url})
            except url_shorten.DoesNotExist:
                short_url = str(uuid.uuid4()).split("-")[0]
                obj = url_shorten(orgin_url=url, 
                                 short_url=short_url)
                obj.save()
                return render(request, 'url-short/massage.html', {'short_url':short_url})
        else:
            return render(request, 'url-short/request.html', {'form':form}) 

class redirectView(views.View):
    def get (self, request, uuid):
        try:
            obj = url_shorten.objects.get(short_url=uuid)
            return redirect(obj.orgin_url)
        except url_shorten.DoesNotExist:
            return redirect("urlshorter:index")