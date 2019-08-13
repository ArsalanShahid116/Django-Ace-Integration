from django.shortcuts import render
from django.http import HttpResponse
from .forms import CodeForm 
from .models import Code

def add_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Program added to database')
        else:
            return HttpResponse('not valid')
    else:  # display empty form
        form = CodeForm()
    
    return render(request, 'coder/add_code.html', {'code_form': form})

