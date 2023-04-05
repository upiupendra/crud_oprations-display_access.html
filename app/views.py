from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',d)

def display_Webpage(request):
    LOT=Webpage.objects.all()
    d={'Web':LOT}
    return render(request,'display_Webpage.html',d)
