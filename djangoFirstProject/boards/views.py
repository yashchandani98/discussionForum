from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards,'i':1})
    board_names = list()
    for board in boards:
        board_names.append(board.name)

    responseSend = '<br/>'.join(board_names)

    return HttpResponse(responseSend)
def boardDetails(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'topics.html',{'board':board})
def createTopic(request,pk):
    board = get_object_or_404(Board,pk=pk)
    return render(request,'newTopic.html',{'board':board})