from django.shortcuts import render, get_object_or_404,  redirect
from django.utils import timezone
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm


def index(request):
    questionList = Question.objects.order_by('-create_date')
    context = {'questionList': questionList}
    return render(request, 'pybo/questionList.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/questionDetail.html', context)

def answer_create(request, question_id):
    '''
    pybo 답변등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/questionDetail.html', context)
    '''
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)
    '''

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pybo/questionForm.html', context)