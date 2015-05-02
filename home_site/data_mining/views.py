from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
    return HttpResponse("<form enctype=\"multipart/form-data\" method=\"post\" action=\"/foo/\"> \n <input type=\"file\" name=\"image\" /> <INPUT name=\"pclog\" type=\"button\" value=\"kmeans\" onClick=\"location.href=\'http://127.0.0.1:8000/kmeans\'\"> ")
