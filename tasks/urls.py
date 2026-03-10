from django.urls import path
from . import views

urlpatterns = [
    path('tasks',views.get_tasks),
    path('tasks/<int:id>',views.update_task),
    path('tasks/<int:id>/report',views.task_report),
]