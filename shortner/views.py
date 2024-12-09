from django.shortcuts import render, redirect
from django.http import JsonResponse
import uuid
import qrcode
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import os
from .models import Url

def create(request):
    print('create request', request.POST)
    if request.method == 'POST':
        
        link = request.POST.get('link')
        uid = str(uuid.uuid4())
        new_url = Url(link=link, uuid=uid)
        print('new_url', new_url)
        new_url.save()

        return HttpResponse(uid)
    else:
        return HttpResponseRedirect('/')

def index(request):
    print('request', request.method)
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        link = request.POST.get('link')
        print('link', link)
        uid = str(uuid.uuid4())
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def expiry_create(request):
    if request.method == 'POST':
        link = request.POST['link']
        expiry_date = parse_datetime(request.POST['expiry_date'])
        uid = str(uuid.uuid4())
        url = Url(link=link, uuid=uid, expiry_date=expiry_date)
        url.save()
        return JsonResponse({'uuid': uid})

def qr_create(request):
    print('qr payload :', request)
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())
        url = Url(link=link, uuid=uid)
        url.save()
        print('url', url)
        # Generate QR Code
        qr = qrcode.QRCode()
        qr.add_data(f"http://127.0.0.1:8000/{uid}")
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        qr_path = f"media/qr_codes/{uid}.png"
        img.save(qr_path)
        print('imag :',img, 'OK', qr_path)
        url.qr_code = qr_path
        url.save()
        return JsonResponse({'uuid': uid, 'qr_code': qr_path})

def password_create(request):
    
    if request.method == 'POST':
        link = request.POST['link']
        password = request.POST['password']
        uid = str(uuid.uuid4())
        url = Url(link=link, uuid=uid, password=password)
        url.save()
        return JsonResponse({'uuid': uid})

def go(request, pk):
    try:
        url_details = Url.objects.get(uuid=pk)
        print('url_details',url_details)
        # Redirect to the actual URL
        return redirect(url_details.link)
    except Url.DoesNotExist:
        return HttpResponse("The requested URL does not exist or has expired.", status=404)
