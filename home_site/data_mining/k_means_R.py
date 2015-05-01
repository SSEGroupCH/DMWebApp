from django.shortcuts import render
from django.template.loader import render_to_string
import os

# Create your views here.
from django.http import HttpResponse

from rpy2.robjects import r

r.source('KMeanS.R')

def output(request):

    return render('k_means_output.html')
