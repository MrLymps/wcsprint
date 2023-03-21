from django.db import models


# Create your models here.py


#class Gallery(models.Model):
#    img_title = models.CharField(max_length=100)
#    img_desc = models.CharField(max_length=500)
#    image = models.ImageField(upload_to='home/')


# class Applications(models.Model):
#     full_name = models.TextField()
#     added_time = models.TimeField()
#     phone_number = models.IntegerField()
#     email = models.EmailField()
#     application_type = models.ForeignKey(ApplicationType, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"ID number : {self.id} "