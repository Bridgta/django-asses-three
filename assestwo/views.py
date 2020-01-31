from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'home.html', {'widgets': widgets, 'widget_form': widget_form})

def add_widget(request):
    if request.method == 'POST':
        widget_form = WidgetForm(request.POST)
        if widget_form.is_valid():
            new_widget = widget_form.save()
            return redirect('home')

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
    def get (self, *args, **kwargs):
        return self.post(*args, kwargs='pk')