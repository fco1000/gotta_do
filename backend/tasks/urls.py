from django.urls import path
from tasks import views

urlpatterns = [
    path('create/',views.TaskCreate.as_view(),name="task-create"),
    path('update/<int:pk>/',views.TaskRetrieveUpdateDestroy.as_view(),name="task-update"),
]
