from django.urls import path
from .views import landing_page, contact_submit

urlpatterns = [
    path('', landing_page, name='landing page'),
    # path('/contact-us/', contact_submit, name='Contact us page', methods=['POST']),
]