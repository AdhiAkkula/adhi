from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def guddi(request):
    return HttpResponse('this is guddi calling')