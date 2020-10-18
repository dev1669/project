from django.shortcuts import render
from django.http import HttpResponse
from .models import Imagetest,Imagetext
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET

# Create your views here.
@login_required
def home(request):
    credential = User.objects.get(username=request.user.username)
    data1 = Imagetext.objects.all()
    data = Imagetest.objects.all()
    context_data={
        'datas' : data,
        'datas1' : data1,
    }
    if credential.is_authenticated:
        return render(request,'index.html',context_data)
   #if credential.is_authenticated and credential.is_staff:
    #    return HttpResponse("Sorry you are not a super user.........")

def tbl(request):
    url = "http://json-gen.com/rest/service/get/oASFyaHhIr6Gg9ptHO5kj"
    data = urllib.request.urlopen(url).read()
    books = ET.fromstring(data)
    book_list = []

    for book in books:
        book_dict = {}
        book_dict.update({'title':book[0].text,'author':book[1].text,'year':book[2].text,'price':book[3].text})
        book_list.append(book_dict)

    return render(request,'xml.html',{'books':book_list})