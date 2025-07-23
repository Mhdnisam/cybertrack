from django import forms
from .models import UserProfile
from .models import HrProfile
from .models import Task
from django.contrib.auth.models import User
from .models import Attendance
from .models import Request
from django.forms import DateInput
from .models import LeaveApplication
from .models import Feedback







class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'password', 'dob', 'address', 'phone_number', 'image']
        widgets = {
            'password': forms.PasswordInput(),  
            'dob': forms.DateInput(attrs={'type': 'date'}), 
            'address': forms.Textarea(attrs={'rows': 3}),  
        }


class HrProfileForm(forms.ModelForm):
    class Meta:
        model = HrProfile
        fields = ['name', 'username', 'password', 'dob', 'address', 'phone_number', 'image']
        widgets = {
            'password': forms.PasswordInput(),  
            'dob': forms.DateInput(attrs={'type': 'date'}), 
            'address': forms.Textarea(attrs={'rows': 3}),  
        }        


from.models import clientdetails
class UserForm(forms.ModelForm):
    class Meta:
        model=clientdetails
        fields='__all__'
      



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'deadline', 'submission_date', 'employees', 'is_completed']

    employees = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_active=True), required=True)



class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['attended']

    attended = forms.ChoiceField(
        choices=[('present', 'Present'), ('absent', 'Absent')],
        widget=forms.RadioSelect,
        label="Mark your attendance",
        initial='absent',  
    )


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['leave_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(LeaveApplicationForm, self).__init__(*args, **kwargs)
        self.fields['leave_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['reason'].widget.attrs.update({'class': 'form-control', 'rows': 4})




class RequestForm(forms.ModelForm):
    request_date = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'date-picker'}),
        required=True,
    )

    class Meta:
        model = Request
        fields = ['title', 'description', 'request_date']  


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'description']



