from django.test import TestCase
from tasksapp.models import Task
from tasksapp.views import update
from tasksapp.views import delete
from tasksapp.views import search
from django.utils import timezone
from django.http import HttpRequest


# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(event="General Event", name="Fundraising Task", description="Collect money for an event",
                            assignee="Bob", duedate="2018-12-30", reporter="Alice", status="Assigned",
                            updatedate=timezone.now())
        Task.objects.create(event="Social Event", name="Decorate Hall", description="Organize event and food",
                            assignee="Alice", duedate="2018-11-29", reporter="Alex", status="Ongoing",
                            updatedate=timezone.now())

    def test_update_task(self):
        task = Task.objects.get(event="Social Event")
        self.assertEqual(task.name, "Decorate Hall")
        request = HttpRequest()
        request.method = 'POST'
        request.POST["eventName"] = "Old age people event"
        request.POST["task"] = "decorate their houses"
        request.POST["duedate"] = "2018-12-31"
        update(request, task.id)
        self.assertEqual(task.name, "Decorate Hall")

    def test_delete_task(self):
        task = Task.objects.get(event="General Event")
        self.assertEqual(len(Task.objects.all()), 2)
        delete(request=None, taskId=task.id)
        self.assertEqual(len(Task.objects.all()), 1)

