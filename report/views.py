from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReportForm
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.db.models import Avg, Max, Min, Sum
from django.contrib import messages

# Create your views here.


def createReportForm(request):

    if request.method == 'POST':
        form = ReportForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, '../templates/report/reportform.html', {'form': form})

    else:
        form = ReportForm()
        return render(request, '../templates/report/reportform.html', {'form': form})
