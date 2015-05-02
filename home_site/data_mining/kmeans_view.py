from django.shortcuts import render
from django.template.loader import render_to_string
import os

# Create your views here.
from django.http import HttpResponse

def output(request):
    html = "<img src=\"static/plot.jpg\" alt=\"kmeans output\"/>"
    return HttpResponse(html)
    #return render(request, 'data_mining/k_means_output.html', {"foo": "bar"},
    #    content_type="application/xhtml+xml")
