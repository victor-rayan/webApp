from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import CreateForm


def createForm(request):

    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateForm()
        return render(request, '../templates/avaliations/createavaliation.html', {'form': form})
