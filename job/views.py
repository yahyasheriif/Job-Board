from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

def job_list(request):
    job_list= Job.objects.all()
    pagintor= Paginator(job_list, 1)
    page_number= request.GET.get('page')
    page_obj= pagintor.get_page(page_number)
    context={'jobs':page_obj,'count':job_list}
    return render(request, "job/job_list.html", context)
def job_detail(request, slug):
    job_detail= Job.objects.get(slug=slug)
    context= {'job':job_detail}
    return render(request, "job/job_detail.html", context)