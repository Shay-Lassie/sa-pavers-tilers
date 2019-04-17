from django.shortcuts import render


def post_list(request):
    return render(request, 'home.html', {})

def about_page(request):
    return render(request, 'about.html', {})

def service_page(request):
    return render(request, 'service.html', {})

def contact_page(request):
    return render(request, 'contact.html', {})
    
def blog_page(request):
    return render(request, 'blogg.html', {})


# Create your views here.
