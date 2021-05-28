from django.shortcuts import render
from .models import TablesNews
# Create your views here.
def index(request):
    blog = TablesNews.objects.all()
    data = {
        "blog":blog
    }
    return render(request, 'index.html', {'data':data})

def view(request, id=None):
    blog = TablesNews.objects.filter(id=id)
    data = {
        "blog":blog
    }
    return render(request, 'view.html', {'data':data})
