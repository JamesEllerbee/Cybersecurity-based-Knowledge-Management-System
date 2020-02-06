from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import assetDropdown
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
