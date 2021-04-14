from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateForm
from django.views.generic import ListView, DetailView
from .models import Avaliation
from django.urls import reverse_lazy, reverse

class HomeView(ListView):
    model = Avaliation
    template_name = 'home.html'
    
   # def get_context_data(self, *args, **kwargs):
        #identfy = get_object_or_404(Avaliation, id = self.kwargs[])
        #context["total_likes"] = total_likes
        #return context

class AvaliationDetailView(DetailView):
    model = Avaliation
    template_name = '../templates/avaliations/avaliation_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AvaliationDetailView, self).get_context_data(*args, **kwargs)
        identfy = get_object_or_404(Avaliation, id=self.kwargs['pk'])
        total_likes = identfy.total_likes()
        context["total_likes"] = total_likes
        return context

def createForm(request):

    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateForm()
        return render(request, '../templates/avaliations/createavaliation.html', {'form': form})


def likeView(request, pk):
    avaliation = get_object_or_404(Avaliation, id=request.POST.get('avaliation_id'))
    avaliation.likes.add(request.user)
    return HttpResponseRedirect(reverse('avaliationDetail', args=[str(pk)]))