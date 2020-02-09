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

@login_required
def question(request):
    #TODO do something with the question. right submitting the text form goes back to this, but we might want to consider going to a different function since POST method is already does something here. -joey
    if request.method == "POST":
        assetID = request.POST["selectedElement"]
        assetName = get_object_or_404(dbAsset, id = assetID)
        questionInputField = inputTextField()

        context = {
            "selectedAsset":assetName,
            "inputTextField":questionInputField,
        }
        return render(request, 'question.html', context)
    else:
        return render(request, 'error.html', {'errorMessage':'Unexpected request'})

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
