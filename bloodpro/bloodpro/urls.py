from django.contrib import admin
from django.urls import path
from blood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', views.submit_form, name='submit_form'),
    path('forms/', views.display_forms, name='display_forms'),
    path('', views.blood_group_counts, name='blood_group_counts'),
]
    