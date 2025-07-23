from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import User





from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=60,null=True,blank=True)  
    password = models.CharField(max_length=255,null=True,blank=True)  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default='2000-01-01')
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.password = make_password(self.password) 
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """
        Custom method to check if the raw password matches the stored hashed password
        """
        return check_password(raw_password, self.password)

from django.contrib.auth.models import User



class HrProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=60,null=True,blank=True)  
    password = models.CharField(max_length=255,null=True,blank=True)  
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    dob = models.DateField(default='2000-01-01')
    address = models.TextField(default="address")
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.password = make_password(self.password) 
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """
        Custom method to check if the raw password matches the stored hashed password
        """
        return check_password(raw_password, self.password)

from django.contrib.auth.models import User
class clientdetails(models.Model):
    username=models.CharField(max_length=20,null=False,default="username")
    password=models.CharField(max_length=20,null=False,default="password")
    phone=models.CharField(max_length=20,null=False)      
    address=models.CharField(max_length=20,null=False)
    location=models.CharField(max_length=20,null=False)  


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(default=timezone.now)
    submission_date = models.DateTimeField(null=True, blank=True)
    employees = models.ManyToManyField(User)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name




from django.contrib.auth.models import User

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {'Present' if self.attended else 'Absent'}"



from django.contrib.auth.models import User


class LeaveApplication(models.Model):
    LEAVE_CHOICES = [
        ('sick', 'Sick Leave'),
        ('vacation', 'Vacation Leave'),
        ('casual', 'Casual Leave'),
    ]
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_applications')
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type} from {self.start_date} to {self.end_date}"
    

from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    request_date = models.DateTimeField()  # Changed to DateTimeField
    approved = models.BooleanField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db import models

class Feedback(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title