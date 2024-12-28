from django.db import models
from django.utils.text import slugify
class Job(models.Model):
    title = models.CharField(max_length=100)
    JOB_TYPE = (
        ("Full Time","Full Time"),
        ("Part Time","Part Time")
    )
    job_type = models.CharField(max_length=100,choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    vacancy= models.IntegerField(default=1)
    salary= models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def upload_img():
        return "jobs/%y/%m/%d"
    image = models.ImageField(upload_to=upload_img ())
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)
class Category(models.Model):
    name= models.CharField(max_length=25)
    def __str__(self):
        return self.name
