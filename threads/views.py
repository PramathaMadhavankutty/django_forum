from django.shortcuts import render,get_object_or_404
from threads.models import Subject
# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html',{'subjects':Subject.objects.all()})

def threads(request,subject_id):
    subject = get_object_or_404(Subject,pk=subject_id)
    return render(request,'forum/threads.html',{'subject':subject})


