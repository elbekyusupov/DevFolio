from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('info', views.InfoPage.as_view(), name='info'),
    path('person', views.PersonPage.as_view(), name='person'),
    path('name', views.get_name, name='name'),
    path('update_person/<int:id>', views.UpdatePerson.as_view(), name='update_person'),
    path('delete_person/<int:id>', views.DeletePerson.as_view(), name='delete_person'),
]