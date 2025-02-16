from django.urls import path
from . import views

app_name = "data_import"
urlpatterns = [
    path('upload/', views.upload_excel, name='upload_excel'),
]
