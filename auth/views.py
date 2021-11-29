from  django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse


def password_changed(request):
    messages.add_message(request, messages.INFO, 'Password changed succesfully')
    return redirect(reverse('profile:home'))
