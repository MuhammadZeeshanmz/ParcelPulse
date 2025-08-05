# from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Create your views here.
def landing_page(request):
    return render(request, "landing/index.html")


def contact_submit(request):
    return render(request, "landing/contact_us.html")    