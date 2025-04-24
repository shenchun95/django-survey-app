from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import SurveyForm
from .models import Survey

def home(request):
    return render(request, 'home.html')

def survey_form(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SurveyForm()
    return render(request, 'form.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def dashboard(request):
    surveys = Survey.objects.all()
    total = surveys.count()
    avg_age = surveys.aggregate(Avg('age'))['age__avg'] or 0
    
    context = {
        'total': total,
        'avg_age': avg_age,
    }
    return render(request, 'dashboard.html', context)