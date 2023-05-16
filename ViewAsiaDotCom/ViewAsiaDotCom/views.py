from django.shortcuts import render, redirect
from ViewAsia.models import *



def searchImg(request):
    if request.method=='GET':
        search_title = request.GET.get('searchtitle').lower()
        
    data = {
        'title': search_title,
        'images': ViewImages.objects.filter(title__contains = search_title),
    }
    return render(request, 'index.html', data)

def viewHome(request):
    data = {
        'title': 'Home Page',
        'images': ViewImages.objects.all().order_by('-id'),
    }
    return render(request, 'index.html', data)

def viewAbout(request):
    data = {
        'title': 'About Page'
    }
    return render(request, 'about.html', data)

def viewContact(request):
    data = {
        'title': 'Contact Page'
    }

    try:
        if request.method == 'POST':
            form = ContactModel()
         
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            created_at = request.POST.get('created_at')
    
            form.name = name
            form.email = email
            form.subject = subject
            form.message = message
            form.created_at = created_at
            form.save()
             
            return render(request, 'contact.html', data)

    except Exception as e:
        print(e)

    return render(request, 'contact.html', data)

def viewLogin(request):
    data = {
        'title': 'Login Page'
    }
    return render(request, 'login.html', data)

def viewSignup(request):
    data = {
        'title': 'Signup Page'
    }
    return render(request, 'signup.html', data)

def viewSubscription(request):
    data = {
        'title': 'Subscription Page'
    }
    return render(request, 'subscription.html', data)

def viewUpload(request):
    try:
        if request.method == 'POST':
            image = request.FILES['image']
            name = request.POST.get('name')
            date = request.POST.get('datetime')
            
            
            UploadModel.objects.create(
                name = name, image = image, 
                date = date
            )

            return redirect('/upload/')
        
    except Exception as e:
        print(e)

    data = {
        'title': 'Upload Page'
    }
    return render(request, 'upload.html', data)