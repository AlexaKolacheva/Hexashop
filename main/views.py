from django.shortcuts import render
from .models import Callback
from .forms import CallbackForm

<<<<<<< HEAD

def callbacks(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()
    return render(request, 'main/contact.html', {'form': form})
=======
def index(request):
    return render(request, 'main/index.html')


>>>>>>> 71f8e1e (authorization and html)
