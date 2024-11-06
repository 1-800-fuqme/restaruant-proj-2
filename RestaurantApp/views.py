from django.shortcuts import HttpResponse, render, loader, redirect
# Create your views here.

def test(request):
    template=loader.get_template('test.html')
    return HttpResponse(template.render())
# use this to test features before making changes to other files

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def account(request):
    template=loader.get_template('account.html')
    return HttpResponse(template.render())

def blog(request):
    template=loader.get_template('blog.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())

def cookbook(request):
    template=loader.get_template('cookbook.html')
    return HttpResponse(template.render())

def menu(request):
    template=loader.get_template('menu.html')
    return HttpResponse(template.render())
