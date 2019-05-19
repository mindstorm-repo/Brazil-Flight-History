from django.urls import include, path

from .views import import_history

app_name = 'core'

urlpatterns = [
    path('import/', import_history, name='import_history'),
]
