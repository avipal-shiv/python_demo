from django.shortcuts import render, HttpResponse
# Create your views here.


def index(request):   
     
    return render(request, 'index.html', )

def error_404_view(request, exception):
   
    return render(request, '404.html')    