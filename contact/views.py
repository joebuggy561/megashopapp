from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from . models import Contact

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact_first_name = request.POST.get('first_name')
        contact_last_name = request.POST.get('last_name')
        contact_email = request.POST.get('email')
        contact_phone_number = request.POST.get('phone_number')
        contact_description = request.POST.get('description')
        contact.first_name = contact_first_name
        contact.last_name = contact_last_name
        contact.email = contact_email
        contact.phone_number = contact_phone_number
        contact.description = contact_description
        contact.save()
        messages.success(request, 'Thank you for Contacting Us. One of our Agents will get to you in the next 24-48hrs')
        # return redirect(request, 'contact')
    else:
        contact = Contact()

    return render(request, 'contacts/contact.html')