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
		eventName = request.POST.get("eventName","")
		taskName = request.POST.get("task","")
		taskDesc = request.POST.get("desc","")
		assignedTo = request.POST.get("assignee","")
		date = request.POST.get("duedate","")
		reporterName = request.POST.get("reporter","")
		state = request.POST.get("status","")
		record = Task(event=eventName, name=taskName, description=taskDesc, assignee=assignedTo, duedate = date,
					reporter = reporterName, status = state,
					updatedate = timezone.now())
		record.save()
		return redirect('/')

def delete(request, taskId):
	record = Task(id=taskId)
	record.delete()
	return redirect('/')

def edit(request, taskId):
	task = Task.objects.get(id=taskId)
	return render(request, "update.html", {'task':task})

def update(request, taskId):
	task = Task.objects.get(id=taskId)
	task.event = request.POST.get("eventName","")
	task.name = request.POST.get("task","")
	task.description = request.POST.get("desc","")
	task.assignee = request.POST.get("assignee","")
	task.duedate = request.POST.get("duedate","")
	task.reporter = request.POST.get("reporter","")
	task.status = request.POST.get("status","")
	task.updatedate = timezone.now()
	task.save()
	return redirect('/')

def search(request):
	eventName = request.POST.get("eventName")
	taskName = request.POST.get("task")
	assignedTo = request.POST.get("assignee")
	date = request.POST.get("duedate")
	state = request.POST.get("status")
	objects = Task.objects.all()
	if eventName.strip():
		objects = objects.filter(event__icontains=eventName)
	if taskName.strip():
		objects = objects.filter(name__icontains=taskName)
	if assignedTo.strip():
		objects = objects.filter(assignee__icontains=assignedTo)
	if state.strip():
		objects = objects.filter(status=state)
	return render(request, "index.html", {'tasks':objects.order_by('duedate')})