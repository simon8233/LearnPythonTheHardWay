from django.shortcuts import render
from datetime import datetime
def hello_world(request):
    return render(request,'hello_world.html',{'current_time':datetime.now()})
# rennder function provide http response.
"""
    render ( request , template_name , dictionary )
"""
# Create your views here.
