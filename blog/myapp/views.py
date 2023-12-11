from django.shortcuts import render
from .forms import blog


# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    form = blog()
    if request.method == 'POST':
        form = blog(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'create.html', context)
