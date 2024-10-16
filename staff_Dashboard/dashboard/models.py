from django.db import models

# Create your models here.
class staff(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=255,null=True,blank=True)
    s_surname=models.CharField(max_length=255,null=True,blank=True)
    s_email=models.EmailField(null=True,blank=True)
    s_age=models.IntegerField(null=True,blank=True)
    s_contact=models.IntegerField(null=True,blank=True)
    s_address=models.TextField(null=True,blank=True)
    s_profile=models.CharField(max_length=255,null=True,blank=True)
    s_subject=models.CharField(max_length=255,null=True,blank=True)
    gender=[
        ("female","female"),
        ("male","male"),
        ("other","other"),
    ]
    s_gender=models.CharField(max_length=255,choices=gender)


    def __int__(self):
        return self.s_id