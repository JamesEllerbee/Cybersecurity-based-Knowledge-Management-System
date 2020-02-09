from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#rom .forms import assetDropdown
from .forms import *
from .models import Asset as dbAsset
from .models import  Threat as assetThreat

from django.shortcuts import get_object_or_404 #used for rapid development, can change later -joey
from django.shortcuts import get_list_or_404 #used for pulling multiple objects from the db - joey

@login_required
def index(request):
    numAssets = dbAsset.objects.all()
    Asset = assetDropdown()
    dropdown = {
        'numAsset':numAssets,
        'Assets': Asset,
    }
    return render(request, 'index.html', dropdown)

def answer(request):
    #TODO implement seraching algo. and return results
    if request.method == "POST":
        print(request.POST)
        question = request.POST["question"]
        context = {
            'function':'Search Results functionality',
            'output': "question = " + question
        }
        return render(request, 'filler.html', context)
    else:#method == "GET"
        return render(request, 'error.html', {'errorMessage': 'Unexpected request for this page'})


@login_required
def question(request):
    if request.method == "POST":
        assetID = request.POST["selectedElement"]
        assetName = get_object_or_404(dbAsset, id = assetID)
        questionInputField = inputTextField()

        context = {
            "selectedAsset":assetName,
            "inputTextField":questionInputField,
        }
        return render(request, 'question.html', context)
    else:#method == "GET"
        return render(request, 'error.html', {'errorMessage':'Unexpected request for this page'})

@login_required
def threats(request):
    assetID = request.POST["selectedElement"]
    assetName = get_object_or_404(dbAsset, id = assetID)
    threats = get_list_or_404(assetThreat, assetKey = assetName)
    context = {
        'selectedAsset': assetName,
        'threats' : threats,
    }
    return render(request, 'common-threats.html', context)
