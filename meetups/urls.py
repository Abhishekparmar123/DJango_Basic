from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'),    # our domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetups_details, name='meetups-details'),  # our domain.com/meetups/<dynamic path segment>
    ]
