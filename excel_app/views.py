from django.shortcuts import render,HttpResponse
import xlrd
import pandas as pd
from excel_app.models import Test_Excel
import datetime
from django.core.paginator import Paginator
from excel_app.forms import UserForm

# Create your views here.

def load_excel(request):
    wb = xlrd.open_workbook('/Users/c100-110/Desktop/Django_Excel_CSV/excel_test/media/data.xlsx')
    sheet = wb.sheet_by_index(0)
    for r in range(sheet.nrows):
        name = sheet.cell(r,0).value
        address = sheet.cell(r,1).value
        visit = sheet.cell(r,2).value
        t = Test_Excel()
        t.name = name
        t.address = address
        t.visit = visit
        t.status = 0
        t.save()
        
    return HttpResponse('Hello')

def show_data(request):
    data = Test_Excel.objects.all()
    # page = request.GET.get('page',1)
    # paginator = Paginator(data,3)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)

    # for i in data:
    #     d = Test_Excel.objects.get(id=i.id)
    #     d.status = 0
    #     d.save()
    return render(request,'excel_app/show_data.html',{'data':data})

def update_status(request,did):
    data = Test_Excel.objects.all()
    t = Test_Excel.objects.get(id=did)
    if t.visit == 1:
        t.status = t.status + 1
    elif t.visit == 2:
        t.status = t.status + 1
    t.save()
    return render(request,'excel_app/show_data.html',{'data':data})

# def status(request):
#     today = datetime.date.today()
#     monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
#     c = 0
#     if mon:
#         c = c + 1
#         if c == 1:
#             t = Test_Excel()

def signup(request):
    user_form = UserForm()
    return render(request,'excel_app/signup.html',{"user_form":user_form})