from django.shortcuts import render
from tasksapp.models import Task
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.


def index(request):
	if request.method == 'GET':
		objects = Task.objects.all().order_by('duedate')
		return render(request, "index.html", {'tasks':objects})
	elif request.method == 'POST':
		taskName = request.POST.get("task","")
		taskDesc = request.POST.get("desc","")
		assignedTo = request.POST.get("assignee","")
		date = request.POST.get("duedate","")
		reporterName = request.POST.get("reporter","")
		state = request.POST.get("status","")
		record = Task(name=taskName, description=taskDesc, assignee=assignedTo, duedate = date, 
					reporter = reporterName, status = state, 
					updatedate = timezone.now())
		record.save()
		return redirect('/')

