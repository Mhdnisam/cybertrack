from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name=''),


# PROJECT MANAGER:-

  path('project_manager_login/', views.project_manager_login_view, name='project_manager_login'),


  path('project_manager_dashboard/', views.project_manager_dashboard_view, name='project_manager_dashboard'),


# USER:-
  path('register/', views.register, name='register'),

  path('login/', views.login_view, name='login'),

  path('user_dashboard/', views.user_dashboard, name='user_dashboard'),



# HR:-


  path('hr_register/', views.hr_register, name='hr_register'),


  path('hr_login/', views.hr_login, name='hr_login'),

  path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),




# CLIENT:-

    path('client_register/', views.client_view, name='client_register'),  # Registration page URL
    path('client_login/', views.clientlogin, name='client_login'),

  path('clientdashboard/', views.client_dashboard, name='clientdashboard'),




# TASK:-

  path('tasks/', views.task, name='task'),

  path('create_task/', views.create_task, name='create_task'),

  path('task_list/', views.task_list, name='task_list'),  
   
   path('user_tasks/', views.user_tasks, name='user_tasks'),


# ATTENDANCE:-

path('attendance/', views.attendance, name='attendance'),

path('submit_attendance/', views.submit_attendance, name='submit_attendance'),

path('attendance-list/', views.attendance_list, name='attendance_list'),

path('attendance_view/', views.attendance_view, name='attendance_view'),



# LEAVE:-

path('leave/', views.leave, name='leave'),

 path('apply_leave/', views.apply_leave, name='apply_leave'),


path('leave_response/', views.leave_response, name='leave_response'),

 path('leave_status/', views.leave_status, name='leave_status'),


# USERPROFILE:-

path('profile/', views.view_profile, name='view_profile'),

path('profile/edit/', views.edit_profile, name='edit_profile'),



# DETAILS ENTRY:-

path('deatails', views.view_details, name='details'),


path('submit/', views.submit_request, name='submit_request'),

    path('manage_requests/', views.manage_requests, name='manage_requests'),

     path('view_own_request/', views.view_own_request, name='view_own_request'),  

#feedback
 path('feedback/', views.submit_feedback, name='submit_feedback'),
 path('view-feedback/', views.view_feedback, name='view_feedback'),












]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
