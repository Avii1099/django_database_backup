from django.shortcuts import render,redirect
from django.contrib import messages
from .models import StudentModel
from django.conf import settings
base_dir = settings.BASE_DIR
from datetime import datetime
from django.core.management import call_command
import os


def HomeView(request):
    all_students = StudentModel.objects.all()
    context = {'all_students':all_students}
    return render(request,'index.html',context)


def DeletedataView(request):
    StudentModel.objects.all().delete()
    messages.error(request,'Students all data deleted')
    return redirect("/")

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
        messages.success(request,'Dabase backup success')
        return redirect('/')




def LoadBackupView(request):
    if request.method == "POST":
        data_file = request.POST.get('data_file')
        f_path = os.path.join(base_dir,'Backup',data_file)
        call_command("loaddata",f_path)
        messages.info(request,'Dabase backup success')
        return redirect('/')
    else:
        return render(request,'index.html')