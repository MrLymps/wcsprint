from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.



def welcome(request):
    return render(
        request,
        'pages/welcome_site.html'
    )


def index(request):
    return render(
        request,
        'pages/index.html'
    )


def about_me(request):
    return render(
        request,
        'pages/about_me.html'
    )


def services(request):
    return render(
        request,
        'pages/services.html'
    )


def gallery(request):
    return render(
        request,
        'pages/gallery.html',

    )



def contact(request):
    return render(
        request,
        'pages/contact.html'
    )


def toilets(request):
    return render(
        request,
        'pages/toilets.html'
    )


def toilet_furniture(request):
    return render(
        request,
        'pages/toilet_furniture.html'
    )


def shower_cabins(request):
    return render(
        request,
        'pages/shower_cabins.html'
    )


def form_app_saving(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        # service = request.POST['service']
        email = request.POST['email']

        subject = 'New order'
        message = f'Prośba o kontakt od osoby - {full_name}, \n' \
                  f'numer telefonu - {phone_number} \n' \
                  f'email - {email} \n'

        if subject and message:
            try:
                send_mail(subject, message, email, ['wcsprint@wp.pl'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/pages/form_app_save')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'pages/form_app_save.html')


def mobile_index(request):
    return render(
        request,
        'pages/mobile_index.html'
    )


def mobile_about_me(request):
    return render(
        request,
        'pages/mobile_about_me.html'
    )