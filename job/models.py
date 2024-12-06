from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    JOB_TYPE = (
        ("Full Time","Full Time"),
        ("Part Time","Part Time")
    )
    job_type = models.CharField(max_length=100,choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    punlished_at = models.DateTimeField(auto_now=True)
    vacancy= models.IntegerField(default=1)
    salary= models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    
    def upload_img():
        return "jobs/%y/%m/%d"
    image = models.ImageField(upload_to=upload_img ())
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name= models.CharField(max_length=25)
    def __str__(self):
        return self.name
