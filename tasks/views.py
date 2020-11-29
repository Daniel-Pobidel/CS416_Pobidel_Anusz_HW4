from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


# CRUD Operations: Create, Retrieve, Update, Delete


# index
def view_tasks(request):
    # Retrieve all the tasks and render tasks.html with the data
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


# add
def create_task(request):
    # Create a form instance and populate it with data from the request
    form = TaskForm(request.POST or None)

    # if request.method == 'POST':
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        print('form valid: true')
    else:
        print('form valid: false')
        print(form.errors)

    # after saving redirect to view_task page
    return redirect('view_tasks')

    # if the request does not have post data, a blank form will be rendered
    # return render(request, 'tasks/tasks.html', {'form': form})


'''
def add_todo(request):
    # Create a form instance and populate it with data from the request
    form = TaskForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()

    # if the request does not have post data, a blank form will be rendered
    return render(request, 'tasks/update.html', {'form': form})
'''


# update
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
    return render(request, 'tasks/update.html', {'form': form, 'task': task})


# delete
def delete_task(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        task.delete()
        # after deleting redirect to view_task page
        return redirect('view_tasks')

    # if the request is not post, render the page with the task's info
    return render(request, 'tasks/delete.html', {'task': task})


# complete
def complete_task(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)

    # if this is a POST request, Task gets marked as completed and saved to database
    if request.method == 'POST':
        task.completed = True
        task.save()

    # after complete redirect to view_task page
    return redirect('view_tasks')
