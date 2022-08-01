from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
	todo = Todo.objects.all().order_by('date','time')
	if request.method == 'POST':
		new_todo = Todo(
			date = request.POST['date'],
			time = request.POST['time'],
			title = request.POST['title']
			)
		new_todo.save()
		return redirect('/')
	return render(request, 'index.html',{'todos':todo})


def delete(request,pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()
	return redirect('/')
