from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def about(request):
  return render(request,"index.html")

def elearn(request):
  return render(request, "elearn.html")