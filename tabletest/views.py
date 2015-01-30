from django.shortcuts import render
from tabletest.models import Person

# Create your views here.
def people(request):
    return render(request, "tabletest/people.html", {"people": Person.objects.all()})