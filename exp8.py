<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Index</title>
</head>
<body>
<form method="POST" class="post-form" enctype="multipart/form-data">
{% csrf_token %}
{{ form.as_p }}
<button type="submit" class="save btn btn-default">Save</button>
</form>
</body> </html> def emp(request):
if request.method == "POST":
form = EmployeeForm (request.POST) if form.is_valid ():
try: return redirect ('/') except:
pass
else:
form = EmployeeForm ()
return render (request,'index.html',{'form':form}) from django import forms from
myapp.models import Employee

class EmployeeForm (forms.ModelForm): class Meta:




model = Employee fields = " all "
from django.db import models class Employee (models.Model):
eid = models.CharField (max_length=20) ename = models.CharField (max_length=100) econtact = models.CharField (max_length=15) class Meta:
db_table = "employee"