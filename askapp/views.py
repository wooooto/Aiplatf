from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm

@login_required
def askwrite(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('askapp:asklist')
    else:
        form = QuestionForm()
    return render(request, 'askapp/write.html', {'form': form})

def asklist(request):
    questions = Question.objects.all()
    return render(request, 'askapp/list.html', {'questions': questions})


