from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import CreateForm
from .models import Avaliation


def createForm(request):

    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateForm()
        return render(request, '../templates/avaliations/createavaliation.html', {'form': form})


def updateForm(request, pk):
    edit = Avaliation.objects.get(id=pk)
    form = CreateForm(instance=edit)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return (redirect('/'))

    context = {'form': form}
    return render(request, '../templates/avaliations/createavaliation.html', context)


def deleteForm(request, pk):
    delete = Avaliation.objects.get(id=pk)

    if request.method == "POST":
        delete.delete()
        return redirect('/')

    context = {'item': delete}
    return render(request, '../templates/avaliations/deleteavaliation.html', context)
