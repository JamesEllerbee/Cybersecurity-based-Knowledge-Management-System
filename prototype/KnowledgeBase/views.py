from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#rom .forms import assetDropdown
from .forms import *
from .models import Asset as dbAsset

@login_required
def index(request):
    numAssets = dbAsset.objects.all()
    Asset = assetDropdown()
    dropdown = {
        'numAsset':numAssets,
        'Assets': Asset,
    }
    return render(request, 'index.html', dropdown)

@login_required
def question(request):
    if request == POST:
        assetID = request.POST["selectedElement"]
        #TODO need to pull asset form DB
        questionInputField = inputTextField()
        context = {
            "selectedAsset":assetID, #TODO change to information pulled from database
            "inputTextField":questionInputField,
        }
        return render(request, 'question.html', context)
    else:
        return(request, 'error.html', {'errorMessage':'Unexpected request'})


@login_required
def threats(request):
    assetID = request.POST["selectedElement"]
    return render(request, 'filler.html', {'function':'Common threats','output':'assetID =' + assetID})
