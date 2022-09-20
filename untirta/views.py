from django.shortcuts import render

# Create your views here.
def coba(request):
    return render(request, 'index.html')