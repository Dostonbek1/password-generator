from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, "generator/home.html")

def password(request):
    alph = "abcdefghijklmnopqrstuvwxyz"
    # add lowercase characters
    chars = list(alph)

    if request.GET.get("uppercase"):
        # add uppercase characters
        chars.extend(list(alph.upper()))

    if request.GET.get("special"):
        # add special characters
        chars.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        # add numbers
        chars.extend(list("01234567789"))

    pass_length = int(request.GET.get("pass_length", 12))
    generated_password = ""

    for i in range(pass_length):
        generated_password += random.choice(chars)

    return render(request, "generator/password.html", {"password": generated_password})