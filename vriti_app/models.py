from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#abc
#category_id, categr_name
#pk, abc, user, pswd, email 

#employer(employer_id, username, psd, email)
#employee(employee_id, username, psd, email)
class Category(models.Model):
    # category_id = models.IntegerField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

