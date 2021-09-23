from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    '''meetups = [
        {
            'title': 'A first Meetups',
            'location': 'New York',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A second Meetups',
            'location': 'Paris',
            'slug': 'a-second-meetup'}
    ]'''
    return render(request, 'meetups/index.html', {
        'show-meetups': True,
        'meetups': meetups
    })


def meetups_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            print(meetup_slug)
            registration_form = RegistrationForm()
            '''selected_meetup = {
                'title': 'A first Meetup',
                'description': 'This is the first meeting!'
            }'''
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, flag = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup_details.html',
                      {'meetup_title': selected_meetup.title,
                       'meetup_description': selected_meetup.describe,
                       'meetup': selected_meetup,
                       'found': True,
                       'form': registration_form
                       })

    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup_details.html', {'found': False})


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/success.html', {'organizer_email': meetup.org_email})
