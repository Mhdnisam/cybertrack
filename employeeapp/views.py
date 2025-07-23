from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserProfileForm
from .forms import HrProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile  
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  
from django.utils import timezone
from .models import Task
from django.http import Http404
from .forms import TaskForm
from .models import UserProfile
from .models import HrProfile
from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Attendance
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Attendance
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RequestForm
from .models import Request
from django.shortcuts import render, redirect
from .forms import LeaveApplicationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import LeaveApplication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FeedbackForm










def index(request):
    return render(request,'index.html')


#  ADMIN:-


USERNAME='employment'
PASSWORD='12345'
def project_manager_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username==USERNAME and password==PASSWORD:
            return redirect('project_manager_dashboard')
        else:
            messages.error(request, "")
    
    return render(request, 'project_manager_login.html')



def project_manager_dashboard_view(request):
    return render(request,'project_manager_dashboard.html')


# USE:-


def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)  

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            username=request.POST.get('username')


            if UserProfile.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different one.')
                return redirect('register')  
            try:
                user_obj=User.objects.create_user(username=username,password=password)
            except Exception as e:
                print(e)
                return render(request, 'register.html')
            user = form.save(commit=False)
            user.user=user_obj
            user.save()


            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')  
        else:
            print(form.errors)

    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request,username=username,password=password)

            if user.check_password(password):
                login(request,user)
                request.session['user_id'] = user.id
                request.session['username'] = user.username

                messages.success(request, 'Login successful!')
                return redirect('user_dashboard')  
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login') 

        except UserProfile.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  

    return render(request, 'login.html')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')








# HR:-




def hr_register(request):
    if request.method == 'POST':
        form = HrProfileForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            username=request.POST.get('username')


            if HrProfile.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different one.')
                return redirect('hr_register')  
            try:
                user_obj=User.objects.create_user(username=username,password=password)
            except Exception as e:
                print(e)
                return render(request, 'hr_register.html')
            user = form.save(commit=False)
            user.user=user_obj
            user.save()


            messages.success(request, 'Registration successful! Please login.')
            return redirect('hr_login')  
        else:
            print(form.errors)

    else:
        form = HrProfileForm()

    return render(request, 'hr_register.html', {'form': form})




def hr_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request,username=username,password=password)

            if user.check_password(password):
                login(request,user)
                request.session['user_id'] = user.id
                request.session['username'] = user.username

                messages.success(request, 'Login successful!')
                return redirect('hr_dashboard')  
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('hr_login') 

        except HrProfile.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('hr_login')  

    return render(request, 'hr_login.html')



def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')





# CLIENT:-

from . models import clientdetails
from.forms import UserForm 
def client_view(request):
    if request.method== 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_login')
    else:
        form=UserForm()
    return render(request,'clientregister.html',{'form':form})

def clientlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = clientdetails.objects.get(username=username)
            if user.password == password:  # In a real-world scenario, use password hashing!
                request.session['user_id'] = user.id  # Store user ID in the session
                messages.success(request, f"Welcome, {username}!")
                return redirect('clientdashboard')  
            else:
                messages.error(request, "Incorrect password.")
        except clientdetails.DoesNotExist:
            messages.error(request, "Username does not exist.")
    return render(request, 'clientlogin.html') 





def client_dashboard(request):
    return render(request, 'client_dashboard.html')




# TASK:-



def task(request):
    return render(request, 'task.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task, UserProfile

def create_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        employee_id = request.POST.get('employee_id')

        task = Task.objects.create(
            task_name=task_name,
            description=description,
            deadline=deadline,
        )

        emp = get_object_or_404(UserProfile, id=employee_id)
        task.user = emp  
        task.save()

        messages.success(request, "Task created successfully!")
        
        return redirect('task_list')  

    users = UserProfile.objects.all()
    return render(request, 'create_task.html', {'users': users})




def task_list(request):
    tasks = Task.objects.all()

    if not tasks.exists():
        return render(request, 'task_list.html', {'message': "There are no tasks assigned yet."})

    return render(request, 'task_list.html', {'tasks': tasks})






@login_required
def user_tasks(request):
    user = request.user

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task_action = request.POST.get('task_action')  

        try:
            task = Task.objects.get(id=task_id, user__user=user)

            if task_action == 'complete':
                task.is_completed = True
            elif task_action == 'pending':
                task.is_completed = False
            task.save()

        except Task.DoesNotExist:
            return redirect('user_tasks')  

    tasks = Task.objects.filter(user__user=user)

    if not tasks.exists():
        return render(request, 'user_task.html', {'message': "You don't have any tasks assigned."})

    return render(request, 'user_task.html', {'tasks': tasks})




# ATTENDANCE:-




def attendance(request):
    return render(request, 'attendance.html')



def attendance_view(request):
    selected_date = request.GET.get('attendance_date', timezone.now().date())

    attendance_data = Attendance.objects.filter(date=selected_date)

    return render(request, 'attendance_view.html', {
        'selected_date': selected_date,
        'attendance_data': attendance_data,
    })



def submit_attendance(request):
    today = date.today() 
    user = request.user  

    attendance, created = Attendance.objects.get_or_create(user=user, date=today)

    if request.method == 'POST':
        attendance_status = request.POST.get('attended')
        if attendance_status == 'present':
            attendance.attended = True
        elif attendance_status == 'absent':
            attendance.attended = False
        attendance.save()  

        return redirect('attendance_list')

    return render(request, 'submit_attendance.html', {'attendance': attendance, 'today': today})



def attendance_list(request):
    user = request.user

    current_date = timezone.now().date()

    attendance_records = Attendance.objects.filter(user=user)

    selected_date = request.GET.get('date', current_date)

    try:
        if isinstance(selected_date, str):
            selected_date = timezone.datetime.strptime(selected_date, '%Y-%m-%d').date()
    except ValueError:
        selected_date = current_date

    attendance_records = attendance_records.filter(date=selected_date)

    return render(request, 'attendance_list.html', {
        'attendance_records': attendance_records,
        'selected_date': selected_date,
        'today': timezone.now().date(),




    })
   

#    LEAVE:-

def leave(request):
    return render(request,('leave.html'))


def apply_leave(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave_application = form.save(commit=False)
            leave_application.employee = request.user  # Associate the logged-in user as the employee
            leave_application.save()
            messages.success(request, 'Your leave application has been submitted successfully.')
            return redirect('leave_status')
    else:
        form = LeaveApplicationForm()

    return render(request, 'apply_leave.html', {'form': form})




@login_required
def leave_response(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        leave_id = request.POST.get('leave_id')
        leave_application = get_object_or_404(LeaveApplication, id=leave_id)

        if action == 'approve':
            leave_application.status = 'Approved'
            leave_application.save()
            messages.success(request, f"Leave application for {leave_application.employee.username} has been approved.")
        elif action == 'reject':
            leave_application.status = 'Rejected'
            leave_application.save()
            messages.success(request, f"Leave application for {leave_application.employee.username} has been rejected.")
        
        return redirect('leave_response')  

    leave_applications = LeaveApplication.objects.filter(status='Pending')
    return render(request, 'leave_response.html', {'leave_applications': leave_applications})



@login_required
def leave_status(request):
    leave_applications = LeaveApplication.objects.filter(employee=request.user)
    return render(request, 'leave_status.html', {'leave_applications': leave_applications})



# USERPROFILE:-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def view_profile(request):
    # Retrieve the current user's profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    # Pass the profile to the template
    return render(request, 'view_profile.html', {'profile': user_profile})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def edit_profile(request):
    # Get the current user's profile
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()  # Save the form data to update the profile
            return redirect('view_profile')  # Redirect to view profile after saving
    else:
        form = UserProfileForm(instance=user_profile)  # Prefill the form with current profile data

    return render(request, 'edit_profile.html', {'form': form})




# DETAILS ENTRY:-



def view_details(request):
    return render(request,('details.html'))


@login_required
def submit_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user  
            form.save()
            return redirect('view_own_request')  
    else:
        form = RequestForm()

    return render(request, 'submit_request.html', {'form': form})



@login_required
def manage_requests(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')

        if request_id and action:
            try:
                req = Request.objects.get(id=request_id)
                if action == 'approve':
                    req.approved = True
                elif action == 'reject':
                    req.approved = False
                req.save()
            except Request.DoesNotExist:
                pass  

    requests = Request.objects.all()

    requests_with_user_info = [
        {
            'request': req,
            'user_name': req.user.username,  
            'user_first_name': req.user.first_name,
            'user_last_name': req.user.last_name,
        }
        for req in requests
    ]

    return render(request, 'manage_requests.html', {'requests': requests_with_user_info})


#feedback

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_feedback')  # Replace with your desired redirect
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

from django.shortcuts import render
from .models import Feedback

def view_feedback(request):
    # Get all feedback, ordered by the date they were submitted (latest first)
    feedback_list = Feedback.objects.all()
    
    # Pass the feedback to the template
    return render(request, 'view_feedback.html', {'feedback_list': feedback_list})




@login_required
def view_own_request(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'view_own_request.html', {'requests': requests})