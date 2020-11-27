from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# CRUD Operations: Create, Retrieve, Update, Delete


def view_tasks(request):
    # Retrieve all the tasks and render tasks.html with the data
    tasks = Task.objects.all()
    context = {'tasks' : tasks}
    return render(request, 'tasks/tasks.html', context)


def create_task(request):
    # Create a form instance and populate it with data from the request
    form = TaskForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_task page
        return redirect('view_tasks')

    # if the request does not have post data, a blank form will be rendered
    return render(request, 'tasks/task-form.html', {'form': form})


def update_task(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=task allows to update the record rather than creating a new record when save method is called
    form = TaskForm(request.POST or None, instance=task)

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_task page
        return redirect('view_tasks')

    # if the request does not have post data, render the page with the form containing the task's info
    return render(request, 'tasks/task-form.html', {'form': form, 'task': task})


def delete_task(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        task.delete()
        # after deleting redirect to view_task page
        return redirect('view_tasks')

    # if the request is not post, render the page with the task's info
    return render(request, 'tasks/delete-confirm.html', {'task': task})