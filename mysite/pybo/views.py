from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    questionList = Question.objects.order_by('-create_date')
    context = {'questionList': questionList}
    return render(request, 'pybo/questionList.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/questionDetail.html', context)