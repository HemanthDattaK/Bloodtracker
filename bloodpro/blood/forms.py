from django import forms

class MyForm(forms.Form):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)
    health_issues = forms.CharField(widget=forms.Textarea, required=False)
