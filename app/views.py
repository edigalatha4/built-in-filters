from django.shortcuts import render
import datetime

# Create your views here.

def filters(request):
    t=datetime.datetime.now()
    d={'data':'hello EVEYone GOOd MOrNinG!!!!','t':t,'c':10}
    return render(request,'filters.html',d)
