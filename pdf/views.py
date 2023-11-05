from django.shortcuts import render
from .models import Profile

# Create your views here.
def accept_view(request):
    return render(request, 'pdf/accept.html')