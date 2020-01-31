from django.forms import ModelForm
from .models import Widget

# Then comes the form for the Widget Model.
class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']