from django.db import models

# The Widget Model only has two fields:

# description - a CharField with a max_length of your choosing
# quantity - an IntegerField


# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()