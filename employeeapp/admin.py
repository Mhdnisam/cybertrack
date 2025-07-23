from django.contrib import admin
from .models import UserProfile
from .models import HrProfile
from .models import Task
from .models import Attendance
from .models import LeaveApplication
from .models import Request,clientdetails
from .models import Feedback


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(HrProfile)
admin.site.register(Task)
admin.site.register(Attendance)
admin.site.register(LeaveApplication)
admin.site.register(Request)
admin.site.register(clientdetails)
admin.site.register(Feedback)

