from django.shortcuts import render

from .forms import BasicForm

# Create your views here.
def crispy_signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass 
    else: 
        form = BasicForm()
    return render(request, 'crispy_signup.html', {'form': form})

    