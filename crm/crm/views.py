from django.conf.global_settings import MEDIA_ROOT
from django.http import JsonResponse

# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task, TaskFile


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        customer = request.POST.get('customer')
        responsible = request.POST.get('responsible')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        status = request.POST.get('status')
        file_list = request.FILES.getlist('files')  # Получение списка файлов

        if not (title and description and customer and responsible and start_date and end_date and status):
            return JsonResponse({'error': 'Заполните все обязательные поля'}, status=400)

        task = Task.objects.create(title=title, description=description, customer=customer, responsible=responsible,
                                   start_date=start_date, end_date=end_date, status=status)

        for file in file_list:
            TaskFile.objects.create(task=task, file=file)

        return JsonResponse({'message': 'Задача успешно создана'})


def history(request):
    tasks = Task.objects.all()
    task_list = []
    for task in tasks:
        task_files = TaskFile.objects.filter(task=task)
        file_urls = [file.file.url for file in task_files]
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'category': task.category,
            'start_date': task.start_date.strftime('%d.%m.%Y'),
            'end_date': task.end_date.strftime('%d.%m.%Y'),
            'responsible': task.responsible,
            'customer': task.customer,
            'status': task.status,
            'files': file_urls,
            # Добавьте другие поля, которые вы хотите отобразить
        }
        task_list.append(task_data)
    return JsonResponse(task_list, safe=False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'category': task.category,
            'start_date': task.start_date.strftime('%d.%m.%Y'),
            'end_date': task.end_date.strftime('%d.%m.%Y'),
            'responsible': task.responsible,
            'customer': task.customer,
            'status': task.status,
            'files': [file.file.url for file in task.taskfile_set.all()]  # Add this line
        }
        return JsonResponse(task_data)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Задача не найдена'}, status=404)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def update_status(request, task_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')

        try:
            task = Task.objects.get(pk=task_id)
            task.status = new_status
            task.save()
            return JsonResponse({'message': 'Статус успешно обновлен'})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Задача не найдена'}, status=404)

    return JsonResponse({'error': 'Неподдерживаемый метод'}, status=405)


@csrf_exempt
def sort_by_responsible(request):
    if request.method == 'GET':
        tasks = Task.objects.order_by('responsible')
        serialized_tasks = [{'id': task.id, 'title': task.title, 'start_date': task.start_date,
                             'end_date': task.end_date, 'responsible': task.responsible,
                             'status': task.status} for task in tasks]
        return JsonResponse(serialized_tasks, safe=False)



def get_task_events(request):
    tasks = Task.objects.all()
    serialized_tasks = [{'id': task.id, 'title': task.title, 'start_date': task.start_date, 'end_date': task.end_date,
    'responsible': task.responsible} for task in tasks]
    return JsonResponse(serialized_tasks, safe=False)

from django.http import JsonResponse
from .models import Task
from django.db.models import Q

def get_employee_data(request):
    employees = ['Иван_Мазур', 'Дима_Винокуров', 'Катя_Сидорина', 'Юра_Черевако']
    employee_data = []

    for employee in employees:
        responsible_filter = Q(responsible__iexact=employee)
        active_tasks = Task.objects.filter(responsible_filter, status__in=['активно', 'в работе']).count()
        completed_tasks = Task.objects.filter(responsible_filter, status__in=['выполнено', 'окончено']).count()
        overdue_tasks = Task.objects.filter(responsible_filter, status__in=['просрочено', 'не выполнено']).count()
        total_tasks = active_tasks + completed_tasks + overdue_tasks
        efficiency = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        employee_data.append({
            'name': employee,
            'activeTasks': active_tasks,
            'completedTasks': completed_tasks,
            'overdueTasks': overdue_tasks,
            'efficiency': efficiency,
        })

    return JsonResponse(employee_data, safe=False)


from django.http import HttpResponse
import os
from django.conf import settings

from django.http import HttpResponse
import os

@csrf_exempt
def download_file(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'task_files', file_name)

    if os.path.exists(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        content_type = None

        if file_extension == '.pdf':
            content_type = 'application/pdf'
        elif file_extension == '.xls':
            content_type = 'application/vnd.ms-excel'
        elif file_extension == '.xlsx':
            content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        elif file_extension == '.doc':
            content_type = 'application/msword'
        elif file_extension == '.docx':
            content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

        if content_type:
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                response['Cache-Control'] = 'no-store, must-revalidate'  # Добавляем эту строку
                return response
        else:
            return HttpResponse('Неподдерживаемый тип файла', status=400)
    else:
        return HttpResponse('Файл не найден', status=404)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt
def upload_report_file(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        report_file = request.FILES.get('report_file')

        if report_file:
            task.report_file = report_file
            task.save()
            return JsonResponse({'message': 'Файл отчета успешно загружен'}, status=200)
        else:
            return JsonResponse({'message': 'Файл отчета не был прикреплен'}, status=400)
    else:
        return JsonResponse({'message': 'Недопустимый метод запроса'}, status=405)
