from itertools import count
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyFormData
from blood import models
from django.db.models import Count


def submit_form(request):
    if request.method == 'POST':
        print("POST request received")
        form = MyForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            MyFormData.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                blood_group=form.cleaned_data['blood_group'],
                health_issues=form.cleaned_data.get('health_issues', '')
            )
            return redirect('display_forms')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        print("GET request received")
        form = MyForm()
    return render(request, 'submit_form.html', {'form': form})

def display_forms(request):
    all_forms = MyFormData.objects.all()
    return render(request, 'display_forms.html', {'forms': all_forms})


def blood_group_counts(request):
    blood_group_counts = MyFormData.objects.values('blood_group').annotate(count=Count('blood_group')).order_by('blood_group')
    return render(request, 'blood_group_counts.html', {'blood_group_counts': blood_group_counts})