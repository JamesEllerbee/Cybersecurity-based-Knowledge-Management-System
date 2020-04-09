from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
# rom .forms import assetDropdown
from .forms import *
from .models import Asset as dbAsset, Question, Answer
from .models import Answer as dbAnswer
from .models import Threat as assetThreat
from .models import Question as dbQuestion
from .models import Answer as dbAnswer
from django.shortcuts import get_object_or_404  # used for rapid development, can change later -joey
from django.shortcuts import get_list_or_404  # used for pulling multiple objects from the db - joey


@login_required
def index(request):
    user = request.user
    print(user.id)
    numAssets = dbAsset.objects.all()
    Asset = assetDropdown()
    dropdown = {
        'numAsset': numAssets,
        'Assets': Asset,
    }
    return render(request, 'index.html', dropdown)

@login_required
def results(request):
    if request.method == "POST":
        question = request.POST["question"]
        request.session['QT'] = question
        assetID = request.session['AID']
        context = {
            'function': 'Search Results functionality',
            'output': question,
            'questions': dbQuestion.objects.filter(assetKey=assetID, questionText__contains=question)

        }
        return render(request, 'results.html', context)
    else:  # method == "GET"
        return render(request, 'error.html', {'errorMessage': 'Unexpected request for this page'})


@login_required
def question(request):
    if request.method == "POST":
        assetID = request.POST["selectedElement"]
        request.session['AID'] = assetID
        assetName = get_object_or_404(dbAsset, id=assetID)
        form = questionInputTextField()
        context = {
            "selectedAsset": assetName,
            "questionInputTextField": form,
        }
        return render(request, 'question.html', context)
    else:  # method == "GET"
        return render(request, 'error.html', {'errorMessage': 'Unexpected request for this page'})


@login_required
def threats(request):
    currentUser = request.user
    assetID = request.POST["selectedElement"]
    assetName = get_object_or_404(dbAsset, id=assetID)
    threats = get_list_or_404(assetThreat, assetKey=assetName)
    context = {

        'selectedAsset': assetName,
        'threats': threats,
        'user': currentUser,
    }
    return render(request, 'common-threats.html', context)

@login_required
def answer(request, question_id):
    questionText = Question.objects.get(id=question_id).questionText
    currentUser = request.user
    answerForm = answerInputTextField()
    context = {
        "questionId": question_id,
        "question": questionText,
        "answers": Answer.objects.all().filter(question=question_id).order_by('-answerRank'),
        "user": currentUser,
        "answerForm": answerForm,
    }
    request.session['QID'] = question_id
    return render(request, 'answer.html', context)

@login_required
def submitQuestion(request):
    if request.method == "GET":
        questionEntry = Question()
        assetID = request.session['AID']
        question = request.session['QT']
        questionEntry.assetKey = get_object_or_404(dbAsset, id=assetID)
        questionEntry.questionText = question
        questionEntry.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'error.html', {'errorMessage': 'Unexpected request for this page'})

@login_required
def submitThreat(request, assetName):
    context = {
        "threatInputTextField": threatInputTextField(),
        "selectedAsset": assetName,
    }
    return render(request, 'threat-form.html', context)

@login_required
def addNewThreat(request, theAssetName):
    threatEntry = assetThreat()
    threatEntry.threatName = request.POST["threat"]
    threatEntry.assetKey = get_object_or_404(dbAsset, assetName=theAssetName)
    threatEntry.save()
    return HttpResponseRedirect("/")

@login_required
def updateScore(request, answer_id, scoreChange):
    question_id = request.session["QID"]
    questionText = Question.objects.get(id=question_id).questionText
    answerForm = answerInputTextField()
    context = {
        "question": questionText,
        "answers": Answer.objects.all().filter(question=question_id).order_by('-answerRank'),
        "questionId": question_id,
        "answerForm": answerForm,
    }
    answerObj = get_object_or_404(dbAnswer, id=answer_id)
    answerObj.answerRank += int(scoreChange)
    answerObj.save()
    return render(request, 'answer.html', context)

@login_required
def addNewAnswer(request, question_id):
    if request == "GET":
        return render(request, 'error.html', {'errorMessage': 'Unexpected request for this page'})
    answerText = request.POST["answer"]
    questionObj = get_object_or_404(dbQuestion, id=question_id)
    answerEntry = dbAnswer()
    answerEntry.answerText = answerText
    answerEntry.question = questionObj
    answerEntry.save()
    context = {
        "response": answerText,
    }
    return render(request, 'submission-success.html', context)

class ThreatDetailView(generic.DetailView):
    model = assetThreat
