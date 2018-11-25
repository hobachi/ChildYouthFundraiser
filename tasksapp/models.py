from django.db import models

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300, default='No Description Available')
	assignee =  models.CharField(max_length=20)
	duedate = models.DateField()
	reporter =  models.CharField(max_length=30)
	status =  models.CharField(max_length=20)
	updatedate = models.DateField(auto_now_add=True)

	class Meta:
		db_table = "tasksdb"