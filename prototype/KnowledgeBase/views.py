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
        'Assets': Asset
    }
    return render(request, 'index.html', dropdown)

def question(request):
    if request.method == "POST":
        
        questionString = request.POST["question"]
        #TODO write serach algo here
        return render(request, 'filler.html', {"output" : questionString}) #change 'filler.html' to a results page and provide the serach results as the context- Joey
    else:
        searchForm = inputTextField()
        return render(request, 'question.html', {"inputTextField": searchForm})