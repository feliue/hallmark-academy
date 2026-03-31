from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentResult


@login_required
def portal(request):
    results = StudentResult.objects.filter(student=request.user)
    return render(request, 'students/portal.html', {'results': results})
