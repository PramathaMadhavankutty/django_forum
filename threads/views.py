from django.shortcuts import render
from threads.models import Subject
# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html',{'subjects':Subject.objects.all()})
