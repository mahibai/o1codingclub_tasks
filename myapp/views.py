# myapp/views.py

from django.shortcuts import render

def task_view(request):
    tasks = []  # Initialize an empty list to store tasks
    
    if request.method == 'POST':
        task_description = request.POST.get('task_description')
        if task_description:
            tasks.append(task_description)  # Add the task to the list
    
    return render(request, 'task.html', {'tasks': tasks})
