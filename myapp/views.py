from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import StudentModel
from django.conf import settings
base_dir = settings.BASE_DIR

from datetime import datetime
from django.core.management import call_command

def HomeView(request):
    
    return render(request,'index.html')


def DataBackupView(request):
    now = datetime.now()
    today_date = now.strftime("%d-%m-%y")
    today_time = now.strftime("(%I-%M-%p)")
    w= str(today_date+"_"+today_time)
    try:
        os.makedirs("Backup")
    except:
        pass
    directory = os.getcwd()
    p = os.path.join(directory,f"Backup\{w}.json")
    with open(p, "w", encoding="utf-8") as fp:
        call_command(f"dumpdata", format="json", indent=3, stdout=fp)
        # messages.success(request,'Dabase backup success')
        return redirect('/')




import os
def LoadBackupView(request):
    if request.method == "POST":
        data_file = request.POST.get('data_file')
        f_path = os.path.join(base_dir,'Backup',data_file)
        call_command("loaddata",f_path)
        # messages.success(request,'Dabase backup success')
        return redirect('/')
