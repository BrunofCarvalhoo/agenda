from django.shortcuts import render,get_list_or_404
from contact.models import Contact
#from django.http import Http404
# Create your views here.
def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')[:10] # seleciona os contatos onde o show é True
    context = {
        'contacts': contacts
    }
    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    
    single_contact = get_list_or_404(Contact,pk=contact_id, show=True) 
           
    context = {
        'contact': single_contact
    }
    return render(
        request,
        'contact/contact.html',
        context
    ) 