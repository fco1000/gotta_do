from django.urls import path
from journal import views

urlpatterns = [
    path('create/',views.JournalCreate.as_view(),name="journal-create"),
    path('update/<int:pk>/',views.JournalRetrieveUpdateDestroy.as_view(),name="journal-update"),
]
