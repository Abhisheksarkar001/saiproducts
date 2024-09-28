from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        return render(request, "index.html")
    except Exception as ex:
        return render(request, "error.html",{"error":ex})
